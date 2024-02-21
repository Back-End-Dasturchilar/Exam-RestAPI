from django.contrib import admin
from .models import (Category,
                     Tag,
                     Post,
                     Comments,
                     ContactInfo,
                     Contact,
                     Author,
                     InstagramImages,
                     Subscribe,
                     Advertise)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Tag),
admin.site.register(Category),
admin.site.register(Contact),
admin.site.register(Comments),
admin.site.register(ContactInfo),
admin.site.register(InstagramImages),
admin.site.register(Subscribe),
admin.site.register(Advertise),





