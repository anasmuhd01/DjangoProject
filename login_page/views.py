from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from login_page.forms import RegistrationForm, LoginForm
from .forms import ItemModelForm
from .models import ItemModel


def home(request):
    username = request.user.username

    image = ItemModel.objects.all()
    context = {'username': username, 'image': image}
    return render(request, "home.html",context)


def user_reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'error_message': 'Email already exists'})
        else:
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
    else:
            form = RegistrationForm()
    return render(request, 'registration.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a profile page or another page after login
            else:
                error_message = 'Invalid username or password'  # Custom error message for incorrect login
        else:
                error_message = 'Invalid username or password'  # You can set a generic error message here for form validation failures
    else:
            form = AuthenticationForm()
            error_message = None

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemModelForm()
        return render(request, 'upload_image.html', {'form':form})
