from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('post/', PostAPIView.as_view(), name='post'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('tag/', TagAPIView.as_view(), name='tag'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('advertise/', AdvertiseAPIView.as_view(), name='advertise'),
    path('instagram/next', InstagramImagesAPIView.as_view(), name='instagram-images'),
    path('comments/', CommentsAPIView.as_view(), name='comments'),
    path('author/', AuthorAPIView.as_view(), name='author'),
    path('detail/<int:pk>/', DetailAPIView.as_view(), name='detail'),
]
