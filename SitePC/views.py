from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

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
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    # context.update({'h1':'ghbdtn'})
    return render(request, "SitePC/index.html", context=context)


def about(request):
    context = {'title': 'Почему мы?',
               'menu': menu}
    return render(request, "SitePC/about.html", context=context)


def helper(request):
    context = {'title': 'Поддержка',
               'menu': menu}
    return render(request, "SitePC/help.html", context=context)


def showPC(request, post_slug):
    product = get_object_or_404(PC, slug=post_slug)
    # product = PC.objects.filter(pk=post_id)
    context = {'title': 'Инфа о товаре',
               'post': product,
               'cat_selected': product.cat_id,
               'menu': menu}
    return render(request, "SitePC/post.html", context=context)


def category(request, cat_slug):
    c = Category.objects.get(slug=cat_slug)
    posts = PC.objects.filter(cat_id=c.id)
    if len(posts) == 0:
        return HttpResponseNotFound('<h1> Страница не найдена </h1>')
    else:
        context = {'title': 'Инфа о товаре',
                   'posts': posts,
                   'cat_selected': c.id,
                   'menu': menu}
        return render(request, "SitePC/index.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
