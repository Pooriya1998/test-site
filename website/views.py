from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def contact_View(request):
    return render(request, 'website/contact.html')
