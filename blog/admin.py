from django.contrib import admin
from .models import Category, Comments, Post, Subscribe, Author, About, Tag, Instagram_images, Advertise_Reklama


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'author')
    search_fields = ['title', 'author']
    filter_horizontal = ['tags']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Subscribe)
admin.site.register(Comments)
admin.site.register(Instagram_images)
admin.site.register(Advertise_Reklama)
