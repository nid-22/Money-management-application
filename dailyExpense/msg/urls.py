from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('first_url', v.firstmethod),
    path('rg', v.rg),
   
    
]