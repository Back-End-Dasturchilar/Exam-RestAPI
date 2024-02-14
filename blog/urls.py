from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeApiView.as_view(), name='home'),
    path('posts/<int:pk>/', DetailApiView.as_view(), name='detail'),
    path('posts/', PostApiView.as_view(), name='posts'),
    path('about/', AboutApiView.as_view(), name='about'),
    path('categories/', CategoryApiView.as_view(), name='categories'),
    path('tags/', TagApiView.as_view(), name='tags'),
    path('authors/', AuthorApiView.as_view(), name='authors'),
    path('advertise/', AdvertiseApiView.as_view(), name='advertise'),
    path('comments/', CommentApiView.as_view(), name='comments'),
    path('subscribe/', SubscribeApiView.as_view(), name='subscribe'),
    path('instagram/', InstagramApiView.as_view(), name='instagram'),
]
