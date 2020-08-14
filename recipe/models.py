from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField


class RecipeContent(models.Model):
    Rec_conId = models.AutoField(primary_key = True)
    # 글번호
    Rec_conName = models.CharField(verbose_name='TITLE', max_length=50)
    # 글제목
    Rec_conReadcount = models.IntegerField(default=0)
    # 조회수
    Rec_conCreate = models.DateTimeField('CREATE_TIME', auto_now_add=True)
    # 작성 시간
    Rec_conModify = models.DateTimeField('MODIFY_DATE')
    # 수정 시간
    Rec_conMemID = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='OWNER', blank=True, null=True)
    # 작성자
    Rec_conPickCount = models.IntegerField(default=0)
    # 찜한 수
    Rec_conContent = HTMLField('CONTENT')
    # 글 내용



class YoutubeContent(models.Model):
    You_conId = models.AutoField(primary_key = True)
    # 글번호
    You_conName = models.CharField(verbose_name='TITLE', max_length=50)
    # 글 제목
    You_conReadcount = models.IntegerField(default=0)
    # 조회수
    You_conCreate = models.DateTimeField('CREATE_TIME', auto_now_add=True)
    # 작성 시간
    You_conModify = models.DateTimeField('MODIFY_DATE')
    # 수정 시간
    You_conMemID = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name='OWNER', blank=True, null=True)
    # 작성자
    You_conPickCount = models.IntegerField(default=0)
    # 찜한 수
    You_conContent = models.TextField('YOUTUBE_CONTENT', default = '')
    # 유튜브 내용(주소)

class Reply(models.Model):
    Rep_id = models.AutoField(primary_key = True)
    # 댓글 번호
    Rep_conid = models.ForeignKey(RecipeContent, on_delete=models.CASCADE, related_name='content_id', blank=True, null=True)
    # 댓글 달 글번호
    Rep_name = models.ForeignKey(RecipeContent, on_delete=models.CASCADE, related_name='content_member', blank=True, null=True)
    # 작성자
    Rep_content = models.TextField('CONTENT')
    # 댓글 내용
    Rep_date = models.DateTimeField(auto_now_add=True)
    # 댓글 작성 시간

