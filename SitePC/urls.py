from django.urls import path

from SitePC.views import index, about, helper, showPC

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('help/', helper, name='helper'),
    path('post/<int:post_id>/', showPC, name = 'post')
]
