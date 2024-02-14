from rest_framework import serializers
from .models import (Author,
                     Post,
                     Advertise,
                     Tag,
                     Category,
                     InstagramImage,
                     Comment,
                     Subscribe)


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class TagSer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class PostSer(serializers.ModelSerializer):
    category = CategorySer()
    tag = TagSer()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class AuthorSer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class AdvertiseSer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class InstaSer(serializers.ModelSerializer):
    class Meta:
        model = InstagramImage
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class CommentsSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']


class SubscribeSer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at']
