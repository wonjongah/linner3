# Generated by Django 3.1 on 2020-08-14 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20200814_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipecontent',
            options={'ordering': ('-Rec_conModify',), 'verbose_name': 'recipe_post'},
        ),
        migrations.AlterModelOptions(
            name='youtubecontent',
            options={'ordering': ('-You_conModify',), 'verbose_name': 'youtube_post'},
        ),
    ]
