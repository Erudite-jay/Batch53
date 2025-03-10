from rest_framework import serializers
from . models import Contact

# class ContactSerializer(serializers.Serializer):
#     full_name=serializers.CharField()
#     phone=serializers.CharField()
#     email=serializers.EmailField()
#     country=serializers.CharField()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields=  '__all__'