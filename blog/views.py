from rest_framework import generics
from .models import Category, Comments, Post, Subscribe, Author, About, Tag

from .serializers import Author_serializer, About_serializer, Category_serializer, Comment_serializer, \
    Subscribe_serializer, Post_serializer, Tag_serializer, Instagram_images


class Author_API_view(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = Author_serializer


class Instagram_images_API_view(generics.ListAPIView):
    queryset = Instagram_images.all()
    serializer_class = Instagram_images


class Tag_API_view(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = Tag_serializer


class Category_API_view(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_serializer


class Comment_APIV_view(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = Comment_serializer


class Post_API_view(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_serializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')
        if q:
            return Post.objects.filter(title__icontains=q)
        if tag:
            return Post.objects.filter(tags__name__icontains=tag)
        if category:
            return Post.objects.filter(category__name__icontains=category)
        else:
            return Post.objects.all()


class About_API_view(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = About_serializer


class Subscribe(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = Subscribe_serializer


class Home_API_view(generics.ListAPIView):
    queryset = Post.objects.all()[:9]
    serializer_class = Post_serializer


class Detail_API_view(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = Post_serializer


class Recent_blogs_API_view(generics.ListAPIView):
    queryset = Post.objects.all()[:3]
    serializer_class = Post_serializer
