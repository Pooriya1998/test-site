from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from blog.models import Post
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_p = form.save(commit=False)
            form_p.name = 'anonymous'
            form_p.save()

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
