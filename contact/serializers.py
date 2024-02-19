from rest_framework import serializers
from .models import Contact, ContactInfo


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read = ['created', 'update']


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        read = ['created', 'update']
