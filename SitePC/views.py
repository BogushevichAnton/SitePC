from urllib import request

from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import generic

from SitePC.models import PC, Orders, Orders_PCs
from SitePC.utils import DataMixin, menu
from accounts.forms import RegisterUserForm, AuthUserForm, UserUpdateForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

from cart.cart import Cart
from cart.forms import CartAddPCForm
from cart.views import cart_search


class Profile(DataMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = "SitePC/profile.html"

    success_url = reverse_lazy('home')

    def get_object(self):
        return get_current_authenticated_user()

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        if len(context['form'].errors) != 0:
            user = get_object_or_404(User, pk=get_current_authenticated_user().id)
            context['user'] = user
            c_def = self.get_user_context(title='Профиль ' + context['user'].email,
                                          user=context['user'])
        else:
            c_def = self.get_user_context(title='Профиль ' + context['user'].email,
                                          user=context['user'])
        return dict(list(context.items()) + list(c_def.items()))


class Home(DataMixin, ListView):
    model = PC
    template_name = "SitePC/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
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
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPC(DataMixin, DetailView):
    model = PC
    template_name = "SitePC/post.html"
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        cart_pc_form = CartAddPCForm()
        context = super().get_context_data(**kwargs)
        key = cart_search(self.request, context['post'].id)
        c_def = self.get_user_context(title='Купить ' + context['post'].title, cat_selected=context['post'].cat_id,
                                      cart_pc_form=cart_pc_form, key=key)
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
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthUserForm
    template_name = 'SitePC/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def order_create(request):
    if request.method == 'POST':
        cart = Cart(request)
        user = get_current_user()
        address = request.POST['address']
        total_price = request.POST['total_price']
        order = Orders()
        order.user = user
        order.price = total_price
        order.address = address
        order.save()
        for item in cart:
            Orders_PCs.objects.create(order=order, pc=item['product'], count=item['quantity'])
        Cart.clear(request)
        return redirect('home')


class Orders_User(DataMixin, ListView):
    model = Orders
    template_name = "SitePC/orders.html"
    context_object_name = 'orders'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        all_Orders_PCS = Orders_PCs.objects.filter()
        c_def = self.get_user_context(title='Ваши заказы', all_Orders_PCS=all_Orders_PCS)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        user = get_current_user()
        orders_user = Orders.objects.filter(user=user)
        return orders_user
