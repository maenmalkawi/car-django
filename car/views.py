from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, Car,News
from django.contrib.auth.decorators import login_required
from .forms import carForms
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Car
from .forms import NewsForm
from django.contrib.auth.decorators import user_passes_test
from .forms import SearchForm


def welcome(request):
    return render(request, 'welcome.html')


def search_view(request):
    results = []
    form = SearchForm(request.GET or None)

    if form.is_valid():  # Check if the form is valid
        query = form.cleaned_data['query']
        # Use your model and field(s) to perform the search
        results = Car.objects.filter(CarModel__icontains=query)  # Adjust 'name' to your field
        print(results)
    return render(request, 'search.html', {'form': form, 'results': results})

@login_required(login_url='login')
def home(request):
    print('test home')


    # Query all cars
    cars = Car.objects.all()

    # Sample user name
    name = "ahmad"

    # Query all users
    users = Users.objects.all()
    

    # Check if the logged-in user is in the 'manager' group
    is_manager = request.user.groups.filter(name__iexact='manegar').exists()

    if is_manager:
        return render(request, 'manager.html')

    # Handle session data for view count
    number_of_views = request.session.get('number_of_views', 0) + 1
    request.session['number_of_views'] = number_of_views

    # Handle session data for logo change
    change_logo = request.session.get('change_logo', 0)
    # if request.method == 'POST':
    #     request.session['change_logo'] = change_logo + 1

    # Context for template
    context = {
        'name': name,
        "worked": is_manager,
        "users": users,
        "number_of_views": number_of_views,
        "change_logo": change_logo,
        "cars": cars,
    }
    if request.method == 'POST':
      search=  request.POST
      form = SearchForm(search)
      print(form)
      if form.is_valid():  # Check if the form is valid
        query = form.cleaned_data['query']
        # Use your model and field(s) to perform the search
        results = Car.objects.filter(CarModel__icontains=query)  # Adjust 'name' to your field
        print(results)
        context['cars']=results
        return render(request, 'home.html', context)
        
        
    

    return render(request, 'home.html', context)

def news(request):
    news = News.objects.all()
    
    return render(request, 'news.html',{'news':news})

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


def is_manager(user):
    return user.groups.filter(name='manegar').exists()  # Replace with your group logic


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addnews')  # Replace 'news_list' with your news page URL name
    else:
        form = NewsForm()
    return render(request, 'addnews.html', {'form': form})
from django.shortcuts import render

# def news_view(request):
#     # Example data for a news article
#     news = {
#         'title': 'Breaking News: Django Simplifies Web Development!',
#         'content': 'Django, the popular Python web framework, continues to simplify the process of building web applications. Developers praise its robustness and flexibility.',
#         'created_at': '2025-02-13',
#     }
#     return render(request, 'news.html', {'news': news})
        

def register(request):
    print('reg')
    if request.method == "POST":
        print("Register view called!")  # Debugging line

        form = RegisterForm(request.POST)
        if form.is_valid():
            print("hello")
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect("login")  # Redirect to home page or another page
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'  # Create this template
    context_object_name = 'car'    