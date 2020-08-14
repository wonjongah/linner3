from django.shortcuts import render

from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView
from hotplace.models import Hotplace
# Create your views here.

class HotplaceLV(ListView):
    model = Hotplace
    template_name = 'hotplace/hotplace_list.html'
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
