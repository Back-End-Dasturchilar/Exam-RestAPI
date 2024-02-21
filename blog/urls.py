from django.urls import path
from .views import (
                    AuthorListApiView,
                    AuthorRetreiveApiView,
                    CategoryListAPIView,
                    PostListAPIView,
                    PostRetreiveApiView,
                    TagListAPIView,
                    CommentListCreateAPIView,
                    CommentRetreiveUpdateDeleteAPIView,
                    ContactInfoAPIView,
                    SubscribeCreateAPIView,
                    InstagramImageRetreiveAPIView,
                    AdvertiseListAPIView
                    )

urlpatterns = [
    path('author/list/', AuthorListApiView.as_view(), name = 'list'),
    path('author/retreive/<int:pk>/', AuthorRetreiveApiView.as_view(), name = 'author-retreive'),
    path('category/', CategoryListAPIView.as_view(), name = 'category-delete'),
    path('posts/', PostListAPIView.as_view(), name = 'post-list'),
    path('post/<int:pk>/', PostRetreiveApiView.as_view(), name = 'post-detail'),
    path('tags/', TagListAPIView.as_view(), name = 'tag-list'),
    path('comments/', CommentListCreateAPIView.as_view(), name = 'comment-list-create'),
    path('comment/<int:pk>/', CommentRetreiveUpdateDeleteAPIView.as_view(), name = 'comment-rud'),
    path('contactinfo/', ContactInfoAPIView.as_view(), name = 'contact-info'),
    path('subscribe/', SubscribeCreateAPIView.as_view(), name = 'subscreibe'),
    path('instagramImage/', InstagramImageRetreiveAPIView.as_view(), name = 'instagram-image'),
    path('advertise/,', AdvertiseListAPIView.as_view(), name = 'advertise-list')


]