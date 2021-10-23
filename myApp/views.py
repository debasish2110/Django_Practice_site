from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("This is home page....!!!")

def About(request):
    return HttpResponse("This is About Page..!!")
