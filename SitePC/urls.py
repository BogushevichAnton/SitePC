from django.urls import path

from SitePC.views import index, about, helper, showPC, category

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('help/', helper, name='helper'),
    path('product/<slug:post_slug>/', showPC, name = 'product'),
    path('category/<slug:cat_slug>', category, name='category'),
]
