from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from blog.models import Post, Category
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "your ticket submited seccessfuly")
        else:
            messages.add_message(request, messages.ERROR, "your ticket didn't submited")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
