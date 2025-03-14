from django.http import JsonResponse
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate,login

# Create your views here.

def login_view(request):
    if request.method=="POST":
        username=request.POST['username'] #data from cleint side
        password=request.POST['password'] #data from cleint side

        user= authenticate(request,username=username, password=password) #Authentication and Authorization
        if user is not None:
            login(request,user) #inbuilt django

            token_data=RefreshToken.for_user(user) # token data

            return JsonResponse({
                "success":True,
                "Message": "User login successfully",
                'refresh': str(token_data),
                'access': str(token_data.access_token)
            })
    return render(request, 'JWT_app/login.html')