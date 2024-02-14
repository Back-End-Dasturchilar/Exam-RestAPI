from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    list_display_links = ['id', 'title', 'created']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Subscribe)
admin.site.register(Advertise)
admin.site.register(Author)

