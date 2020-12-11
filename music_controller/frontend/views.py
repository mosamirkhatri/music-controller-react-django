from django.shortcuts import render

# Create your views here.


def index(request, *args, **kwargs):
    """
    docstring
    """
    return render(request, 'frontend/index.html')
