# Generated by Django 3.2.5 on 2021-07-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='MyBlog', max_length=255),
        ),
    ]
