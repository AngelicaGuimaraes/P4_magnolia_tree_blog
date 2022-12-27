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
