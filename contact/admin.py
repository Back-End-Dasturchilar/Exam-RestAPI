from django.contrib import admin
from .models import Contact, ContactInfo


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_display_links = ['id', 'name', 'created']


admin.site.register(ContactInfo)