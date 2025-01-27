from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Car
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    print('test home')

    # Query all cars
    Cars = Car.objects.all()

    # Sample user name
    name = "ahmad"

    # Query all users
    users = Users.objects.all()
    print(request.user.groups.filter(name="manegar").exists())

    # Check if the logged-in user is in the 'manager' group
    is_manager = request.user.groups.filter(name__iexact='manegar').exists()

    if is_manager:
        return render(request, 'manager.html')

    # Handle session data for view count
    number_of_views = request.session.get('number_of_views', 0) + 1
    request.session['number_of_views'] = number_of_views

    # Handle session data for logo change
    change_logo = request.session.get('change_logo', 0)
    if request.method == 'POST':
        print('Post request received')
        request.session['change_logo'] = change_logo + 1

    # Context for template
    context = {
        'name': name,
        "worked": is_manager,  # Indicate if user is in the 'manager' group
        "users": users,
        "number_of_views": number_of_views,
        "change_logo": change_logo,
        "Cars": Cars,
    }

    return render(request, 'home.html', context)

def news(request):
    return render(request, 'news.html')

def slider(request):
    return render(request, 'slider.html')

@login_required(login_url='login')
def addcars(request) :
    user = request.user
    if user.groups.filter(name='manegar').exists():
    # create a form to add cars from the model cars
        if request.method =='POST':
            pass    
        return render(request, 'addcars.html')
    else:
        return HttpResponse("YOU DONT HAVE PERMISSION TO ADD CAR")
    
    
@login_required(login_url='login')
def addCarInstance(request) :
    user = request.user
    if user.groups.filter(name='manegar').exists():
    # create a form to add cars from the model cars
        if request.method =='POST':
            pass    
        return render(request, 'addcars.html')
    else:
        return HttpResponse("YOU DONT HAVE PERMISSION TO ADD CAR")    