from django.contrib import admin
from django.urls import path
from recipe.views import *


app_name = 'recipe'


urlpatterns = [
    path('', RecipeLV.as_view(), name='recipe_listview'),
    path('post/', RecipeLV.as_view(), name='recipe_listview'),
    path('<int:pk>', RecipeDV.as_view(), name='recipe_detail'),
    path('youtube/<int:pk>', YoutubeDV.as_view(), name='youtube_detail'),
    path('add_recipe/', RecipeCreateView.as_view(), name='recipe_create'),
    path('add_youtube/', YoutubeCreateView.as_view(), name='youtube_create'),

]