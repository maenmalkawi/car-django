from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')

def home(request):
   print('test home')
   name="ahmad"
   users = Users.objects.all()
   print(users)  
   
   # create a sussion that show the user how many he view the home page
   
   # create a variable that store the number of views 
   
   number_of_views = request.session.get('number_of_views',0)
   # increment the number of views
   request.session['number_of_views']=number_of_views +1
   change_logo= request.session.get('change_logo',0)
   if request.method =='POST':
      print('post request')
      request.session['change_logo'] = change_logo +1
      
      pass
   
   context={
      'name':name,
      "worked":False,
      "users":users,
      "number_of_views": number_of_views,
      "change_logo" : change_logo
   }
   return render(request,'home.html',context = context) 

def news(request):
   return render(request,'news.html')

def slider(request):
   return render(request,'slider.html')