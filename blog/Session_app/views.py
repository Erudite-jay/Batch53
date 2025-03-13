from django.http import JsonResponse
from django.shortcuts import render
from . models import User

# Create your views here.


def login(request):
    if request.session.get('usersession'):
        return JsonResponse({
            "message":"Already login",
            "user":request.session.get('usersession')
            #redirect to home ? 
        })

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
            if user.password==password:

                request.session.set_expiry(20)
                request.session['usersession']=username

                return JsonResponse({
                    "success":True,
                    "Message": "User logged in successfully"
                },status=200)
        except Exception as e:
            return JsonResponse({
                    "success":False,
                    "Message": "User failed to login"
                },status=500)
        
    return render(request,'Session_app/login.html')