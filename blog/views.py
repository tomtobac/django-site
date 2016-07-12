u"""
View.

Description.
"""
from django.shortcuts import render
from models import Post


def index(request):
    """Index."""
    posts = Post.objects.filter(published_date__isnull=False)
    return render(request, 'blog/index.html', {'posts': posts})
