from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views
#from . import *

urlpatterns = [
   path('index', views.index, name='index'),
   path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
   path('signup', views.sign_up, name='signup'),
   path('login',views.login, name='login'),
   path('legendary',views.legendary, name='legendary'),
   path('starter',views.starter, name='starter'),
   path('post',views.post, name='post'),

]