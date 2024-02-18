from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactAPIView.as_view(), name='Contact_API_View'),
    path('info/', ContactInfoAPIView.as_view(), name='ContactInfo_API_View'),
    # path('detail/<int:pk>', ContactDetailAPIView.as_view(), name='ContactInfo_API_View'),

]
