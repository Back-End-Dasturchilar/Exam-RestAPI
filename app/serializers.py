from rest_framework import serializers
from .models import (Post,
                     Category,
                     Tag,
                     Subscribe,
                     Advertise,
                     InstagramImages,
                     Comments,
                     Author)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class InstagramImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramImages
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
