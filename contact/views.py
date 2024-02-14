from django.shortcuts import render

from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import ContactSerializers, ContactInfoSerializers


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers