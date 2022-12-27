from django.shortcuts import render


def home_page(request):
    """
    View for home page.
    """
    return render(request, 'index.html')


def classes_page(request):
    """
    View for classes page.
    """
    return render(request, 'classes.html')


def contact_page(request):
    """
    View for contact page
    """
    return render(request, 'contact.html')


class BlogPage(generic.ListView):
    """
    View for blog page. Inspired by "I think therefore I blog"
    from Code Institute
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 7


class BlogPostDetail(View):
    """
    Detailed view of a blogpost. Inspired by "I think therefore I blog"
    frome Code Institute
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates a URL based on the slug of the Blog post
        """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blog-post.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Submit a new comment to a
        blog post.
        """
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                request,
                "Your comment will be reviewd before it's published. "
                )
        else:
            comment_form = CommentForm()

        return render(
            request,
            'blog-post.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class LikeBlogPost(View):
    """
    Class that makes a user be able to like a blogpost.
    Borrowed from "I think therefore I am" project from 
    Code institute.
    """
    def post(self, request, slug):
        """
        Makes sure there is authenticated user
        and allows a like/unlike.
        """
        post = get_object_or_404(BlogPost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog_post', args=[slug]))


class UpdateComment(SuccessMessageMixin, UpdateView):
    """
    View for updateing comment
    """
    model = BlogComment
    form_class = CommentForm
    context_object_name = 'comment'
    template_name = 'update-comment.html'
    success_message = "Your comment is updated"

    def form_valid(self, form):
        """
        Success url return to blog post
        """
        self.success_url = f'/{self.get_object().post.slug}/'
        return super().form_valid(form)


class DeleteComment(DeleteView):
    """
    View for deleting comment
    """
    model = BlogComment
    context_object_name = 'comment'
    template_name = 'delete-comment.html'

    def get_success_url(self, *args):
        """
        Success url return to blog post
        """
        self.success_url = f'/{self.get_object().post.slug}'
        self.slug = self.get_object().post.slug
        return reverse_lazy('blog_post', args=[self.slug])
