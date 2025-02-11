from .views import *
from django.urls import path 
from .views import CarDetailView
from django.http import HttpResponse


urlpatterns = [
   
   path('',home,name='home'),
   path('news/',news,name='news'),
   path('slider/',slider,name='slider'),
   path('addcars/',addcars,name='addcars'),
   path('car/<int:pk>/', CarDetailView.as_view(), name='car'),


   
]