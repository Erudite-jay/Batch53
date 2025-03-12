from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUpload
# Create your views here.

def file_upload(request):
    try:
        if request.method=="POST":
            form=FileUploadForm(request.POST,request.FILES) # getting file data, file name 
            print(form)
            if form.is_valid(): # data is valid

                #normal form
                # record=FileUpload(name=form.cleaned_data['name'],file=form.cleaned_data['file'])  # django shell
                # record.save()

                #model form 
                form.save()

                return JsonResponse({
                    "success":True
                },status=200)
            else:
                return JsonResponse({
                    "Success":False,
                    "Form Error":str(form.errors.as_json()) 
                },status=404)
        else: #if request.method== "GET":
            form=FileUploadForm() # empty form
    except Exception as e:
        return JsonResponse({
            "success":False,
            "Error":str(e)
        },status=500)
    
    return render(request,"Forms_app/fileForm.html",{'form':form})
    