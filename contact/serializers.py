from rest_framework import serializers
from .models import Contact, ContactInfo


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = 'all'
        read = ['created', 'update']


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = 'all'
        read = ['created', 'update']