from django.contrib import admin
from . models import Contact
# Register your models here.

admin.site.register(Contact)

# @admin.register(Contact)
# class ContactData(admin.ModelAdmin):
#     list_display=["id","full_name","phone","email","country"]
#     search_fields=["email"]
