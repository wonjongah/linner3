# Generated by Django 3.1 on 2020-08-17 20:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0007_auto_20200817_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubecontent',
            name='You_conLikesUser',
            field=models.ManyToManyField(blank=True, related_name='You_conLikesUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
