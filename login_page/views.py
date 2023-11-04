from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from .forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["[password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                return render(request, "home.html")



