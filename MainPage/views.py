from django.shortcuts import render
from . import models
def news_view(request):
    post_value = models.Post.objects.all()
    return render(request, 'index.html', {'post_key': post_value})