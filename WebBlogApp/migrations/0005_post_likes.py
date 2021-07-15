# Generated by Django 3.2.5 on 2021-07-14 15:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebBlogApp', '0004_auto_20210712_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
