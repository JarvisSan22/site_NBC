from django.shortcuts import render
from .models import Post,Image,Tag
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    images = Image.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    tags = Tag.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts,"images":images,"tags":tags})
