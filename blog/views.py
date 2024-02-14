from rest_framework import generics
from .models import (Category,
                     Comment,
                     Post,
                     Advertise,
                     Author,
                     About,
                     Tag,
                     Subscribe,
                     Instagram)
# Create your views here.

from .seri import (AuthorSerializer,
                   AboutSerializer,
                   CategorySerializer,
                   CommentSerializer,
                   SubscribeSerializer,
                   PostSerializer,
                   TagSerializer,
                   AdvertiseSerializer,
                   InstagramSerializer)


class AuthorApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagApiView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AdvertiseApiView(generics.ListAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSerializer


class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HomeApiView(generics.ListAPIView):
    queryset = Post.objects.all()[:9]
    serializer_class = PostSerializer


class DetailApiView(generics.ListAPIView):
    queryset = Post.objects.all()[:9]
    serializer_class = PostSerializer


class SubscribeApiView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


class InstagramApiView(generics.ListAPIView):
    queryset = Instagram.objects.all()
    serializer_class = InstagramSerializer
