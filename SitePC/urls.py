from django.urls import path

from SitePC.views import about, helper, Home, Category, ShowPC

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('help/', helper, name='helper'),
    path('product/<slug:slug>/', ShowPC.as_view(), name = 'product'),
    path('category/<slug:cat_slug>', Category.as_view(), name='category'),
]
