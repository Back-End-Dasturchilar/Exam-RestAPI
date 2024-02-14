from  rest_framework import serializers
from .models import (Category,
                     Tag,
                     Post,
                     Comments,
                     Subscribe,
                     Author,
                     Advertise,
                     Instagram,
                     )

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read = ['created', 'update']


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read = ['created', 'update']


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read = ['created', 'update']


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read = ['created', 'update']


class SubscribeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
        read = ['created', 'update']


class InstagramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = '__all__'
        read = ['created', 'update']

class AdvertiseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'
        read = ['created', 'update']


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read = ['created', 'update']

