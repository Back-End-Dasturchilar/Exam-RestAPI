from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import (Category,
                     Tag,
                     Post,
                     Comments,
                     Subscribe,
                     Author,
                     Advertise,
                     Instagram)


class HomeAPIView(generics.ListAPIView):
    queryset = Post.objects.all()[:6]
    serializer_class = PostSerializers


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        title = self.request.query_params.get('title')
        if tag:
            return Post.objects.filter(tag__name__icontains=tag)
        if category:
            return Post.objects.filter(category__name__icontains=category)
        if title:
            return Post.objects.filter(title__name__icontains=title)
        else:
            return Post.objects.all()



class CommentsAPIView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers


class SubscribeAPIView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializers


class AdvertiseAPIView(generics.ListAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSerializers


class InstagramAPIView(generics.ListAPIView):
    queryset = Instagram.objects.all()
    serializer_class = InstagramSerializers


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        author = self.request.query_params.get('author')
        comments = self.request.query_params.get('comments')
        if tag:
            return Post.objects.filter(tag__name__icontains=tag)
        if category:
            return Post.objects.filter(category__name__icontains=category)
        if author:
            return Post.objects.filter(author__name__icontains=author)
        if comments:
            return Post.objects.filter(comment__name__icontains=comments)
        else:
            return Post.objects.all()



