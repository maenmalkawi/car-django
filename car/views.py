from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, Car
from django.contrib.auth.decorators import login_required
from .forms import carForms

@login_required(login_url='login')
def home(request):
    print('test home')

    # Query all cars
    cars = Car.objects.all()

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
        "worked": is_manager,
        "users": users,
        "number_of_views": number_of_views,
        "change_logo": change_logo,
        "cars": cars,
    }

    return render(request, 'home.html', context)

def news(request):
    return render(request, 'news.html')

def slider(request):
    return render(request, 'slider.html')

@login_required(login_url='login')
def addcars(request):
    print('test')
    user = request.user
    print(user.groups.filter(name__iexact='manegar').exists())
    if user.groups.filter(name__iexact='manegar').exists():
        if request.method == 'POST':
            print(request.POST)
            form = carForms(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                print('Car added successfully')
                return redirect('home')  # Fixed missing return statement

        else:
            form = carForms()  # Instantiate empty form for GET request

        return render(request, 'addcars.html', {'form': form})
    else:
        return HttpResponse("YOU DON'T HAVE PERMISSION TO ADD A CAR")

@login_required(login_url='login')
def addCarInstance(request):
    user = request.user
    if user.groups.filter(name__iexact='manegar').exists():
        if request.method == 'POST':
            form = carForms(request.POST)
            if form.is_valid():
                form.save()
                print('Car instance added successfully')
                return redirect('home')  # Ensure redirection after saving

        else:
            form = carForms()  # Instantiate empty form for GET request

        return render(request, 'addcars.html', {'form': form})
    else:
        return HttpResponse("YOU DON'T HAVE PERMISSION TO ADD A CAR")
    