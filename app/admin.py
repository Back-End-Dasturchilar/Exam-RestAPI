from django.contrib import admin
from .models import (Post,
                     Category,
                     Tag,
                     Subscribe,
                     Advertise,
                     InstagramImages,
                     Comments,
                     Author)


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'profession', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'profession')
    search_fields = ['name', 'profession']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'author_name')
    search_fields = ['title', 'author_name']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Subscribe)
admin.site.register(Advertise)
admin.site.register(InstagramImages)
admin.site.register(Comments)
