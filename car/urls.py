from .views import *
from django.urls import path 


urlpatterns = [
   
   path('home/',home,name='home'),
   path('news/',news,name='news'),
   path('slider/',slider,name='slider')
]