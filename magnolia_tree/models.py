"""
Models for Magnolia Tree Blog
"""

from django.db import models

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

        