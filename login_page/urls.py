# appname/urls.py
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/register/", views.user_reg, name="register"),
    path('/profile/', views.profile, name='profile'),
    path('/login/', views.user_login, name='login')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)