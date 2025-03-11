from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Contact
from .Serializers import ContactSerializer
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello world")

def home_page(request):
    return render(request,"Auth_app/index.html")


@csrf_exempt
def all_data(request):
    if request.method=="GET":
        all_user_data=Contact.objects.all() #queryset
        seralized_data=ContactSerializer(all_user_data,many=True) #serialized data
        print(type(seralized_data)) 
        return JsonResponse(seralized_data.data,safe=False) #JSON
    

    if request.method=="POST":
        try:
            input_data=json.loads(request.body) # we are getting data from client 
            serializer_data=ContactSerializer(data=input_data) # deseralization

            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    "success":True,
                    "message":"Data saved successfully"
                },status=201)
            
        except Exception as e:
            return JsonResponse({
                "success":False,
                "error":str(e),
                "message":"fail to save data"
            },status=400)
                
@csrf_exempt
def single_user_data(request,pk):
    if request.method=="GET":
        try:
            user= Contact.objects.get(pk=pk)
            serializer_data=ContactSerializer(user)
            return JsonResponse({
                "success":True,
                "Data":serializer_data.data
            },status=200)
        
        except Exception as e:
             return JsonResponse({
                "success":False,
                "error":str(e)
            },status=400)
    
    if request.method=="PUT":
        try:
            user=Contact.objects.get(pk=pk) #find the user
            input_data=json.loads(request.body) # get the from client

            serializer_data=ContactSerializer(user,data=input_data) # call seraizlzer to update data
            if serializer_data.is_valid():  # validated
                serializer_data.save() # save into DB
            
            return JsonResponse({
                "Success":True,
                "message":"Data updated successfully",
                "Updated Data ": serializer_data.data
            },status=200)
        
        except Exception as e:
            return JsonResponse({
                "success":False,
                "Error":str(e)
            },status=400)
        
    if request.method=="PATCH":
        try:
            user=Contact.objects.get(pk=pk) #find the user
            input_data=json.loads(request.body) # get the from client

            serializer_data=ContactSerializer(user,data=input_data,partial=True) # call seraizlzer to update data
            if serializer_data.is_valid():  # validated
                serializer_data.save() # save into DB
            
            return JsonResponse({
                "Success":True,
                "message":"Data updated successfully",
                "Updated Data ": serializer_data.data
            },status=200)
        
        except Exception as e:
            return JsonResponse({
                "success":False,
                "Error":str(e)
            },status=400)
        
    if request.method=="DELETE":
        try:
            user=Contact.objects.get(pk=pk)
            user.delete()
            
            return JsonResponse({
                "Success":True,
                "message":"Data Deleted successfully",
            },status=200)
        
        except Exception as e:
            return JsonResponse({
                "success":False,
                "Error":str(e)
            },status=400)

