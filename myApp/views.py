from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'variable':"this is the variable sent here..... ;)"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is home page....!!!")

def About(request):
    return render(request, "About.html")
