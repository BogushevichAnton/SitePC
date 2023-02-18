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
    #context.update({'h1':'ghbdtn'})
    return render(request, "SitePC/index.html", context=context)

def gamers(request):
    posts = PC.objects.filter(cat__name='Игровые')
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, "SitePC/index.html", context=context)
def gamers_home(request):
    posts = PC.objects.filter(cat__name='Для офиса и дома')
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, "SitePC/index.html", context=context)
def laptops(request):
    posts = PC.objects.filter(cat__name='Ноутбуки')
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

def category(request, cat_id):
    posts = PC.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        return HttpResponseNotFound('<h1> Страница не найдена </h1>')
    else:
        context = {'title': 'Инфа о товаре',
                   'posts': posts,
                   'menu': menu}
        return render(request, "SitePC/index.html", context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
