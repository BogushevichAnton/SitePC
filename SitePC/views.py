from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import *
from .utils import *
from .forms import *


class Home(DataMixin, ListView):
    model = PC
    template_name = "SitePC/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return PC.objects.all()


class Category(DataMixin, ListView):
    model = PC
    template_name = "SitePC/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return PC.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected = context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPC(DataMixin, DetailView):
    model = PC
    template_name = "SitePC/post.html"
    context_object_name = 'post'
    allow_empty = False

    def get_queryset(self):
        return PC.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Купить ' + context['post'].title, cat_selected = context['post'].cat_id)
        return dict(list(context.items()) + list(c_def.items()))



class About(DataMixin, TemplateView):
    template_name = "SitePC/about.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(c_def.items()))


def helper(request):
    context = {'title': 'Поддержка',
               'menu': menu}
    return render(request, "SitePC/help.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'SitePC/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
