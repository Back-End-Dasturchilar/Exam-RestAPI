from rest_framework import generics, mixins
from .serializers import (TagSerializer,
                     PostSerializer,
                     CommentSerializer,
                     CategorySerializer,
                     AuthorSerializer,
                     InstagramImageSerializer,
                     SubscribeSerializer,
                     AdverticeSerializer,
                    ContactInfoSerializer)

from .models import (Category,
                     Tag,
                     Post,
                     Comments,
                     ContactInfo,
                     Author,
                     InstagramImages,
                     Subscribe,
                     Advertise)

class AdvertiseListAPIView(generics.GenericAPIView,
                           mixins.ListModelMixin):
    queryset = Advertise.objects.all()
    serializer_class = AdverticeSerializer
    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
class InstagramImageRetreiveAPIView(generics.GenericAPIView,
                                mixins.RetrieveModelMixin):

    queryset = InstagramImages.objects.all()
    serializer_class = InstagramImageSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class ContactInfoAPIView(generics.GenericAPIView,
                  mixins.RetrieveModelMixin):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class CommentRetreiveUpdateDeleteAPIView(generics.GenericAPIView,
                                        mixins.UpdateModelMixin,
                                        mixins.RetrieveModelMixin,
                                        mixins.DestroyModelMixin):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentListCreateAPIView(generics.GenericAPIView,
                           mixins.CreateModelMixin,
                           mixins.ListModelMixin):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def list(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class PostListAPIView(generics.GenericAPIView,
                           mixins.ListModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostRetreiveApiView(generics.GenericAPIView,
          mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class TagListAPIView(generics.GenericAPIView,
                           mixins.ListModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AuthorRetreiveApiView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin
                                        ):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,  *args, **kwargs)

class AuthorListApiView(generics.GenericAPIView,
                        mixins.ListModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CategoryListAPIView(generics.GenericAPIView,
                          mixins.ListModelMixin
                          ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class SubscribeCreateAPIView(generics.GenericAPIView,
                             mixins.CreateModelMixin):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

