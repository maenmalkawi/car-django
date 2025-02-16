from .views import *
from django.urls import path 
from .views import CarDetailView
from django.http import HttpResponse
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
   
   path('home',home,name='home'),
   path('news/',news,name='news'),
   path('slider/',slider,name='slider'),
   path('addcars/',addcars,name='addcars'),
   path('car/<int:pk>/', CarDetailView.as_view(), name='car'),
   path('addnews/', views.add_news, name='addnews'),
   # path('news/', views.news_view, name='news'),
   path('search/', views.search_view, name='search'),
   path('', views.welcome, name='welcome'),  # Home page
    path('login/', views.login, name='login'),  # Add your login view here   
    path('', views.welcome, name='welcome'),  # Root URL for the welcome page
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

]
