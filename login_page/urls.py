# appname/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/register", views.user_reg, name="register"),
    path('/profile', views.profile, name='profile'),
    path('/login', views.user_login, name='login'),
    path('/logout', views.user_logout, name='logout'),
    path('/upload', views.upload_product, name='upload'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)