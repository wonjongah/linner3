from django.shortcuts import render

from django.views.generic import ListView,DetailView
from hotplace.models import Hotplace
# Create your views here.

class HotplaceLV(ListView):
    model = Hotplace

class HotplaceDV(DetailView):
    model = Hotplace

