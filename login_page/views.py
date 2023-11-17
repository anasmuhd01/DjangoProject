from _decimal import Decimal

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from login_page.forms import RegistrationForm, LoginForm
from .forms import ItemModelForm
from .models import ItemModel, CartItem, Cart


def home(request):
    username = request.user.username
    image = ItemModel.objects.all()
    context = {'username': username, 'image': image}

    return render(request, "home.html", context)


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


def upload_product(request):
    if request.method == 'POST':
        form = ItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemModelForm()
        return render(request, 'upload_image.html', {'form':form})



# views.py

from django.core.serializers.json import DjangoJSONEncoder
import json

def add_to_cart(request, item_id):
    item = ItemModel.objects.get(id=item_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart = request.session.get('cart', {})
        cart_item = cart.get(str(item_id))  # Convert item_id to string
        if cart_item:
            cart_item['quantity'] += 1
        else:
            cart_item = {
                'title': item.title,
                'price': str(item.price),  # Convert price to string
                'quantity': 1,
            }

        cart[str(item_id)] = cart_item  # Convert item_id to string
        request.session['cart'] = json.loads(json.dumps(cart, cls=DjangoJSONEncoder))

    return redirect('home')


from decimal import Decimal  # Import the Decimal class

def view_cart(request):
    total_price = Decimal(0)  # Initialize total_price as a decimal

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items_in_cart = cart.cartitem_set.all()
        user = request.user
        # Calculate total_price for authenticated users
        total_price = sum(item.item.price * item.quantity for item in items_in_cart)
    else:
        cart = request.session.get('cart', {})
        item_ids = cart.keys()
        items_in_cart = []
        for item_id in item_ids:
            cart_item = cart[item_id]
            item = {
                'title': cart_item['title'],
                'price': Decimal(cart_item['price']),
                'quantity': cart_item['quantity'],
            }
            total_price += item['price'] * item['quantity']
            items_in_cart.append(item)
        user = None

    return render(request, 'cart.html', {'items_in_cart': items_in_cart, 'user': user, 'total_price': total_price})
