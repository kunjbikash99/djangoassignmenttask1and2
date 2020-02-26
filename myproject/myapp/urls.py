from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('cong/',views.cong),
]