from django.views.generic import TemplateView, CreateView, FormView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# 유저
from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied
from .form import CreateUserForm
from recipe.models import RecipeContent, YoutubeContent
from hotplace.models import Hotplace

from django.views.generic import FormView
from django.db.models import Q
from django.shortcuts import render
from .forms import PostSearchForm

from django.contrib.auth.models import User

# 순수하게 html 템플릿만 운영할 수 있도록 도와주는
# 공통 사용할 것~~~~~~~~~~~~~~~~~



class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('signup_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/signup_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.Rec_conMemID:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)

class OwnerOnlyMixin1(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)


class OwnerOnlyMixin2(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.You_conMemID:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)



# --- FormView
class SearchFormView(FormView):


    form_class = PostSearchForm

    template_name = 'post_search.html'

    def form_valid(self, form):


        searchWord = form.cleaned_data['search_word']

# 1
        post_list = RecipeContent.objects.filter(

            Q(Rec_conName__icontains=searchWord) |

            Q(Rec_conContent__icontains=searchWord)

        ).distinct()
# 2

        you_list = YoutubeContent.objects.filter(

            Q(You_conName__icontains=searchWord) |

            Q(You_conContent__icontains=searchWord)

        ).distinct()

# 3

        hot_list = Hotplace.objects.filter(

            Q(title__icontains=searchWord) |

            Q(content__icontains=searchWord)

        ).distinct()




        context = {}

        context['form'] = form

        context['search_term'] = searchWord

        context['recipe_search'] = post_list

        context['youtube_search'] = you_list

        context['hot_search'] = hot_list


        return render(self.request, self.template_name, context)

