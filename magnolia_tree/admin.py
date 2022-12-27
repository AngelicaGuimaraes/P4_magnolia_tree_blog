"""
Classes and functions for the built in Admin in Django
"""

from django.contrib import admin
from django.contrib.sites.models import Site
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Section, BlogPost, BlogComment


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Making it possible to use summernote to create blog posts
    in Admin. Used from "I think therefore I blog" from 
    Code Institute.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Making it possible to read and approve comments
    in Admin. Used from "I think therefore I blog" from 
    Code Institute.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Function to approve pending
        user comments on blog posts
        """
        queryset.update(approved=True)


admin.site.register(Category)
admin.site.register(Section)
