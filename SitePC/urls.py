from django.urls import path

from SitePC.views import index, about, helper, showPC, category

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:cat_id>', category, name = 'category'),
    path('about/', about, name='about'),
    path('help/', helper, name='helper'),
    path('post/<int:post_id>/', showPC, name = 'post')

]
