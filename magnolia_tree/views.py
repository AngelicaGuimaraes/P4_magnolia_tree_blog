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
