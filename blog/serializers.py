from rest_framework import serializers
from .models import Author, About, Category, Comments, Post, Subscribe, Tag, Instagram_images, Advertise_Reklama


class Author_serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class Tag_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Post_serializer(serializers.ModelSerializer):
    author = Author_serializer()
    category = Category_serializer()
    tags = Tag_serializer(many=True)
    comment_set = Comment_serializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'tags', 'author', 'category', 'description', 'comment_set', 'created_at',
                  'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class About_serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Subscribe_serializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Istagram_images(serializers.ModelSerializer):
    class Meta:
        model = Instagram_images
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Advertise_reklama(serializers.ModelSerializer):
    class Meta:
        model = Advertise_Reklama
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
