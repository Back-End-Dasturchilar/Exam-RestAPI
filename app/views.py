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
                     InstagramImages)


class HomeAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()[:6]
    serializer_class = PostSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('category')
        if tag:
            return Post.objects.filter(tag__name__icontains=tag)
        if category:
            return Post.objects.filter(category__name__icontains=category)
        else:
            return Post.objects.all()


class CommentsAPIView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class SubscribeAPIView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class AdvertiseAPIView(generics.ListAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AuthorSerializer


class InstagramImagesAPIView(generics.ListAPIView):
    queryset = InstagramImages.objects.all()
    serializer_class = InstagramImagesSerializer


class AuthorAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
