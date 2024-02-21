from rest_framework import serializers
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
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer()
    comments_set = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']


class AdverticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']

class InstagramImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramImages
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']




class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']





































