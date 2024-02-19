from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from app.models import *
from app.ser import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination, PageNumberPagination

# Create your views here.
class TagPage(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagApi

class CatPage(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatApi

class AdPage(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdApi

class SubPage(CreateAPIView):
    queryset = Sub.objects.all().filter()
    serializer_class = SubApi

class AuthorPage(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorApi

class ContactPage(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContApi

class InfoPage(CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = InfoApi

class CommPage(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ComApi

class PostPage(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi

    def get_queryset(self):
        queryset = Post.objects.all()


        title = self.request.query_params.get('title',None)
        tag = self.request.query_params.get('tag',None)
        author = self.request.query_params.get('author_name',None)
        cat = self.request.query_params.get('cat',None)




        if title:
            queryset = queryset.filter(title__icontains=title)
        if tag:
            queryset = queryset.filter(tag__name__icontains=tag)
        if author:
            queryset = queryset.filter(author_name__icontains=author)
        if cat:
            queryset = queryset.filter(cat__name__icontains=cat)
        else: 
            queryset = Post.objects.all()

        return queryset

class InstaPage(ListCreateAPIView):
    queryset = Insta.objects.all()
    serializer_class = InfoApi

class HomePostPage(ListAPIView):
    queryset = Post.objects.all()[0:6]
    serializer_class = PostApi


class DetailPostPage(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi


class PopularPostPage(ListAPIView):
    queryset = Post.objects.all()[0:4]
    serializer_class = PostApi




