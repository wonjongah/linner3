from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from tinymce.models import HTMLField
#별점
from django.core.validators import MinValueValidator,MaxValueValidator
#태그
from taggit.managers import TaggableManager

# Create your models here.
class Hotplace(models.Model):
    # id = models.IntegerField(verbose_name='HOT_ID', primary_key=True)
    # title = models.CharField('HOT_TITLE', max_length=100)
    # slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text ='one word for title alias.')
    # name = models.CharField('HOT_NAME', max_length=15)
     # 별점
    # content = models.TextField('HOT_CONTENT')  # content = HTMLField('CONTENT')
    # create_dt = models.DateTimeField('HOT_CREATE_DATE', auto_now_add=True)
    # modify_dt = models.DateTimeField('HOT_MODIFY_DATE')

    title = models.CharField('TITLE', max_length=100)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text ='one word for title alias.')
    name = models.CharField('NAME', max_length=15)
    # 별점)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    content = HTMLField('CONTENT')
    create_dt = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY_DATE')

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'hotplace'
        verbose_name_plural = 'hotplaces'
        ordering = ('-modify_dt',)  # -내림차순 orderby절

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ''  #reverse('')


    def get_previous(self):
        return self.get_previous_by_modify_dt()


    def get_next(self):
        return self.get_next_by_modify_dt()
