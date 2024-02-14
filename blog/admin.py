from django.contrib import admin
from .models import (Category,
                     Comment,
                     Post,
                     Subscribe,
                     Author,
                     About,
                     Tag,
                     Advertise,
                     Instagram)


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'author')
    search_fields = ['title', 'author']
    filter_horizontal = ['tags']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Instagram)
admin.site.register(About)
admin.site.register(Author)
admin.site.register(Subscribe)
admin.site.register(Advertise)

