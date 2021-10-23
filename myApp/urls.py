from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.index, name='myApp'),
    path("About",views.About, name="About")
]