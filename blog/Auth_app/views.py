from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Contact
from .Serializers import ContactSerializer
# Create your views here.

def print_hello(request):
    return HttpResponse("Hello world")

def home_page(request):
    return render(request,"Auth_app/index.html")

def all_data(request):
    if request.method=="GET":
        all_user_data=Contact.objects.all() #queryset
        seralized_data=ContactSerializer(all_user_data,many=True) #serialized data
        print(type(seralized_data)) 
        return JsonResponse(seralized_data.data,safe=False) #JSON