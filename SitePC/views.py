from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Поддержка', 'url_name': 'helper'},
        {'title': 'Корзина', 'url_name': 'helper'},
        {'title': 'Вход', 'url_name': 'helper'}
        ]

class Home(ListView):
    model=PC
    template_name = "SitePC/index.html"
    context_object_name='posts'
    allow_empty = False
    def get_context_data(selfself, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главное меню'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return PC.objects.all()


class Category(ListView):
    model=PC
    template_name = "SitePC/index.html"
    context_object_name='posts'
    allow_empty = False
    def get_queryset(self):
        return PC.objects.filter(cat__slug=self.kwargs['cat_slug'])
    def get_context_data(selfself, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class ShowPC(DetailView):
    model=PC
    template_name = "SitePC/post.html"
    context_object_name='post'
    allow_empty = False
    def get_queryset(self):

        return PC.objects.filter(slug=self.kwargs['slug'])
    def get_context_data(selfself, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Купить ' + context['post'].title
        context['cat_selected'] = context['post'].cat_id
        return context
def about(request):
    context = {'title': 'Почему мы?',
               'menu': menu}
    return render(request, "SitePC/about.html", context=context)


def helper(request):
    context = {'title': 'Поддержка',
               'menu': menu}
    return render(request, "SitePC/help.html", context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')
