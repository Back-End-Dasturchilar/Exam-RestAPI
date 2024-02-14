from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


# class ContactDetailAPIView(generics.ListAPIView):
#     queryset = ContactInfo.objects.all()
#     serializer_class = ContactInfoSerializer
