from django import forms
from .models import FileUpload
#normal form 
# class FileUploadForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     file=forms.FileField()


#model form

class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FileUpload
        fields='__all__'