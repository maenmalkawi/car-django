from django.shortcuts import render
from django.http import HttpResponse

from .models import Users
# Create your views here.
def home(request):
   print('test home')
   name="ahmad"
   users = Users.objects.all()
   print(users)  
   
   context={
      'name':name,
      "worked":False,
      "users":users
   }
   return render(request,'home.html',context = context) 