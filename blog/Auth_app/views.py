from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello world")

def home_page(request):
    return render(request,"Auth_app/index.html")