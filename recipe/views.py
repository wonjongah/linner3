from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
# 부모클래스로 리스트뷰(목록보겠다)랑 디테일뷰(한 개를 자세히 보겠다)
from recipe.models import RecipeContent, YoutubeContent

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class RecipeLV(ListView):
    model = RecipeContent
    context_object_name = 'recipe_list'
    template_name = 'recipe/recipe_list.html'

class RecipeDV(DetailView):
    model = RecipeContent
    context_object_name = 'recipe'
    template_name = 'recipe/recipe_detail.html'

class YoutubeDV(DetailView):
    model = YoutubeContent
    context_object_name = 'youtube'
    template_name = 'recipe/youtube_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = RecipeContent
    fields = ['Rec_conName', 'Rec_comReadcount', 'Rec_conMemID', 'Rec_conPickCount', 'Rec_conContent']
    success_url = reverse_lazy('recipe:recipe_listview')
    template_name = 'recipe/recipe_create.html'

class YoutubeCreateView(CreateView):
    model = YoutubeContent
    fields = ['You_conName', 'You_conReadcount', 'You_conMemID', 'you_conPickCount']
    success_url = reverse_lazy('recipe:recipe_listview')
    template_name = 'recipe/youtube_create.html'
