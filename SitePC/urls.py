from django.urls import path

from SitePC.views import helper, Home, Category, ShowPC, About, RegisterUser, LoginUser, logout_user, Profile

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('help/', helper, name='helper'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile'),
    path('product/<slug:slug>/', ShowPC.as_view(), name = 'product'),
    path('category/<slug:cat_slug>', Category.as_view(), name='category'),

]
