from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ItemModel, CartItem, Cart
# Register your models here.

@admin.register(ItemModel)
class MyAdminModel(admin.ModelAdmin):
    list_display = ('title','price')


