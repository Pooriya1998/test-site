from django.shortcuts import render, get_object_or_404
from blog.models import Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def blog_view(request, **kwargs):
    posts = Post.objects.exclude(published_date__gt=datetime.datetime.now())
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    all_cats = Category.objects.all()
    context = context = {'posts': posts, 'all_cats': all_cats}
    return render(request, 'blog/blog-home/blog-home.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    all_cats = Category.objects.all()
    context = {'post': post, 'all_cats': all_cats}
    return render(request, 'blog/blog-single/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home/blog-home.html', context)