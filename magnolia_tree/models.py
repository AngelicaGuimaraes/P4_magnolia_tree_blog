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






       