from django.urls import path
from .views import (HomePage,
                    CommentPage,
                    BlogDetail,
                    BlogPage,
                    AuthorView,
                    TagView,
                    ImageView,
                    CategoryView,
                    SubscribeView, AdvertiseView,
                    )

urlpatterns = [
    path('', HomePage.as_view()),
    path('comment/', CommentPage.as_view()),
    path('detail/', BlogDetail.as_view()),
    path('blog/', BlogPage.as_view()),
    path('author', AuthorView.as_view()),
    path('tag/', TagView.as_view()),
    path('image/', ImageView.as_view()),
    path('category/', CategoryView.as_view()),
    path('subscribe/', SubscribeView.as_view()),
    path('advertise/', AdvertiseView.as_view())
]
