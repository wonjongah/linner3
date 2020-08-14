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
    context_object_name = 'recipe_list'
    template_name = 'recipe/recipe_list.html'
    queryset = RecipeContent.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['youtube_list'] = YoutubeContent.objects.all()
        # 한 뷰에 여러 개 모델 콘텍스트 가져오고 싶을 때!!!!!!!!!!!!!!!!!!!!!!!
        return context


class RecipeDV(DetailView):
    model = RecipeContent
    context_object_name = 'recipe'
    template_name = 'recipe/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # post = context['post']
        recipe_post = self.get_object()
        recipe_post.Rec_conReadcount += 1
        recipe_post.save()
        return context

class YoutubeDV(DetailView):
    model = YoutubeContent
    context_object_name = 'youtube'
    template_name = 'recipe/youtube_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # post = context['post']
        youtube_post = self.get_object()
        youtube_post.You_conReadcount += 1
        youtube_post.save()
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = RecipeContent
    fields = ['Rec_conName', 'Rec_conContent', 'Rec_conTags']
    success_url = reverse_lazy('recipe:recipe_listview')
    template_name = 'recipe/recipe_create.html'

    def form_valid(self, form):
        form.instance.Rec_conMemID = self.request.user
        return super().form_valid(form)


class YoutubeCreateView(LoginRequiredMixin, CreateView):
    model = YoutubeContent
    fields = ['You_conName',  'You_conContent', 'You_conTags']
    success_url = reverse_lazy('recipe:recipe_listview')
    template_name = 'recipe/youtube_create.html'

    def form_valid(self, form):
        form.instance.You_conMemID = self.request.user
        return super().form_valid(form)