from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Home_API_view.as_view(), name='home'),
    path('posts/<int:pk>/', Detail_API_view.as_view(), name='detail'),
    path('posts/', Post_API_view.as_view(), name='posts'),
    path('about/', About_API_view.as_view(), name='about'),
    path('categories/', Category_API_view.as_view(), name='categories'),
    path('tags/', Tag_API_view.as_view(), name='tags'),
    path('authors/', Author_API_view.as_view(), name='authors'),
    path('happy-clients/', Subscribe_serializer.as_view(), name='clients'),
    path('comments/', Comment_APIV_view.as_view(), name='comments'),
    path('recent/', Recent_blogs_API_view.as_view(), name='recent-posts'),
]
