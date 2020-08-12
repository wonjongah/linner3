from django.contrib import admin
from hotplace.models import Hotplace

# Register your models here.

@admin.register(Hotplace)
class HotplaceAdmin(admin.ModelAdmin):
    list_display = ('id','title','modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title','content')
    prepopulated_fields = {'slug':('title',)}
