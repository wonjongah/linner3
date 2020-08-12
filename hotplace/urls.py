from django.urls import path, include
from hotplace.views import HotplaceLV,HotplaceDV

app_name = 'hotplace'

urlpatterns=[
    path('',HotplaceLV.as_view(),name='index'),
    path('<int:pk>/',HotplaceDV.as_view(),name='detail'),



]