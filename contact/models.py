from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address_name = models.TextField()
    phone_number = models.CharField(max_length=212)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
