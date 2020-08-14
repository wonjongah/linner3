from django.shortcuts import render

from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView
from hotplace.models import Hotplace
# for 유저
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin



# Create your views here.

class HotplaceLV(ListView):
    model = Hotplace
    template_name = 'hotplace/hotplace_printlist.html'
    context_object_name = 'hotplaces'


class HotplaceDV(DetailView):
    model = Hotplace

# Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post.html'
    model = Hotplace

    def get_queryset(self):
        return Hotplace.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

class HotplaceAV(ArchiveIndexView):
    model = Hotplace
    date_field = 'modify_dt'

class HotplaceYAV(YearArchiveView):
    model = Hotplace
    date_field = 'modify_dt'
    make_object_list = True

class HotplaceMAV(MonthArchiveView):
    model = Hotplace
    date_field = 'modify_dt'
    month_format = '%m'


class HotplaceCreateView(LoginRequiredMixin,CreateView):
    model = Hotplace
    fields = ['title','slug','rating','content','tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('hotplac:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class HotplaceUpdateView(OwnerOnlyMixin,UpdateView):
    model = Hotplace
    fields = ['title','slug','rating','content','tags']
    success_url = reverse_lazy('hotplace:index')

class HotplaceDeleteView(OwnerOnlyMixin,DeleteView):
    model = Hotplace
    success_url = reverse_lazy('hotplace:index')









