from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from login_page.forms import RegistrationForm, LoginForm


def home(request):
    return render(request, "home.html")


def user_reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
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
                return redirect('profile')  # Redirect to a profile page or another page after login
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