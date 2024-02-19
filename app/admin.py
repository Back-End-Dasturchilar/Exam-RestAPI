from django.contrib import admin
from app.models import *


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['tag']

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(Sub)
admin.site.register(Insta)