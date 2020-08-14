from django.urls import path, include
from hotplace.views import *

app_name = 'hotplace'

urlpatterns=[
    path('',HotplaceLV.as_view(),name='index'),
    path('<int:pk>/',HotplaceDV.as_view(),name='detail'),

    #태그
    # Example :/hotplace/tag
    path('tag',TagCloudTV.as_view(),name='tag_cloud'),
    # Example :/hotplace/tag/tagname/
    path('tag.<str:tag>',TaggedObjectLV.as_view(),name='tagged_object_list'),



]