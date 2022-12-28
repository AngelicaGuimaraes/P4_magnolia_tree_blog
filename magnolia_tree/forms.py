"""
Forms for magnolia tree blog page
"""
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import BlogComment, BlogPost


class CommentForm(forms.ModelForm):
    """
    Form for adding comments
    """
    class Meta:
        model = BlogComment
        fields = ('body',)


class CreateBlogPost(forms.ModelForm):
    """
    Form for creating a blog post
    """
    class Meta:
        """
        States what fields shall be seen in the form
        """
        model = BlogPost
        fields = (
            'title',
            'category',
            'section',
            'content',
            'excerpt',
            'featured_image',
        )
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'title': 'Title of your blogpost',
            'category': 'Chose category',
            'section': 'Chose affected area',
            'content': 'Your post',
            'excerpt': 'Summary',
            'featured_image': 'Upload image',
        }