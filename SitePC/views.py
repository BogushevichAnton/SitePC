from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Поддержка', 'url_name': 'helper'},
        {'title': 'Корзина', 'url_name': 'helper'},
        {'title': 'Вход', 'url_name': 'helper'}
        ]


def index(request):
    posts = PC.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}

    return render(request, "SitePC/index.html", context=context)


def about(request):
    context = {'title': 'Почему мы?',
               'menu': menu}
    return render(request, "SitePC/about.html", context=context)


def helper(request):
    context = {'title': 'Поддержка',
               'menu': menu}
    return render(request, "SitePC/help.html", context=context)


def showPC(request, post_id):
    post = PC.objects.filter(pk=post_id)
    if len(post) == 0:
        return HttpResponseNotFound('<h1> Страница не найдена </h1>')
    else:
        context = {'title': 'Инфа о товаре',
                   'posts': post,
                   'menu': menu}
        return render(request, "SitePC/post.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
