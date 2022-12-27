"""
Models for Magnolia Tree
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Model for categories for blogposts stating category of
    Yoga.
    """
    category_name = models.CharField(
        max_length=200,
        blank=True,
        unique=True,
        help_text='Enter type of yoga'
        )

    class Meta:
        """
        Meta fields for ordering
        """
        ordering = ['category_name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.category_name}'

    def get_absolute_url(self):
        """
        Returns the URL to access a category
        """
        return reverse('category_name', args=[str(self.id)])


class Section(models.Model):
    """
    Model for section of body affected by the yoga
    """
    section_name = models.CharField(
        max_length=200,
        blank=True,
        unique=True,
        help_text='Enter a section of the body'
        )

    class Meta:
        """
        Meta fields for ordering
        """
        ordering = ['section_name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.section_name}'

    def get_absolute_url(self):
        """
        Returns the URL to access a section
        """
        return reverse('section_name', args=[str(self.id)])


class BlogPost(models.Model):
    """
    Model for blog post. This model was inspired by the
    "I think therefore I blog" project by Code Institute.
    """
    title = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField(
        Category, help_text='Select a Yoga category for the blogpost'
        )
    section = models.ManyToManyField(
        Section, help_text='Select a section of body affected'
        )
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        To display blog posts in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        To return a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        To return total number of post likes
        """
        return self.likes.count()
        

class BlogComment(models.Model):
    """
    Model for comments on blogposts inspired by the
    "I think therefore I blog" project by Code Institute.
    """
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=20,
        related_name='comment_author'
        )
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order comments in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Display the comment as the comment text,
        and comment author name
        """
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """
        Returns url based on primary key 
        """
        return reverse('post_detail', kwargs={'pk': self.pk})






       