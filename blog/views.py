from .models import (Author,
                     Post,
                     Advertise,
                     Tag,
                     Category,
                     InstagramImage,
                     Comment,
                     Subscribe)
from .serializers import (AuthorSer,
                          AdvertiseSer,
                          SubscribeSer,
                          PostSer,
                          CategorySer,
                          CommentsSer,
                          TagSer,
                          InstaSer)
from rest_framework import generics


class HomePage(generics.ListAPIView):
    queryset = Post.objects.all()[:6]
    serializer_class = PostSer


class BlogPage(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')

        if tag:
            return Post.objects.filter(tag__name__icontains=tag)


class CommentPage(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentsSer


class BlogDetail(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')
        comments = self.request.query_params.get('com')
        author_name = self.request.query_params.get('author')
        if author_name:
            return Post.objects.filter(author__name__icontest=author_name)
        if tag:
            return Post.objects.filter(tag__name__icontains=tag)
        if comments:
            return Post.objects.filter(comment__name__icontains=comments)
        if category:
            return Post.objects.filter(category__name__icontains=category)

        else:
            return Post.objects.all()


class PopularPost(generics.ListAPIView):
    queryset = Post.objects.all()[:4]
    serializer_class = PostSer


class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSer


class AdvertiseView(generics.ListAPIView):
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySer


class ImageView(generics.ListAPIView):
    queryset = InstagramImage.objects.all()
    serializer_class = InstaSer


class SubscribeView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSer
