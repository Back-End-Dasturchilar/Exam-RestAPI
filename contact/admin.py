from django.contrib import admin
from .models import Contact, ContactInfo


# Register your models here.


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_at')
    list_display_links = ('id', 'name', 'email', 'created_at')
    search_fields = ['name', 'email', 'phone']


admin.site.register(ContactInfo)
