from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article


def index(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, template_name='articles/index.html', context=context)


def show(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, template_name='articles/show.html', context={'article': article})
