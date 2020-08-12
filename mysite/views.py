from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# 순수하게 html 템플릿만 운영할 수 있도록 도와주는
# 공통 사용할 것~~~~~~~~~~~~~~~~~

class HomeView(TemplateView):
    template_name = 'home.html'
