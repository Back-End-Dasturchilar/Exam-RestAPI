from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('tag/', TagAPIView.as_view(), name='tag'),
    path('post/', PostAPIView.as_view(), name='post'),
    path('comments/', CommentsAPIView.as_view(), name='comments'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('advertise/', AdvertiseAPIView.as_view(), name='advert'),
    path('insta/', InstagramAPIView.as_view(), name='insta'),
    path('author/', AuthorAPIView.as_view(), name='author'),
    path('detail/', DetailAPIView.as_view(), name='detail')


]