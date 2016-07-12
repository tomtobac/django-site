u"""
View.

Description.
"""
from django.shortcuts import render


def index(request):
    """Index."""
    return render(request, 'main/index.html', {})
