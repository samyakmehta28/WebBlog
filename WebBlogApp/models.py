from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default = 'miscellaneous')
    likes = models.ManyToManyField(User, related_name="blog")

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    #this function is to get url from "add" button on add_blog.html and helps to add new blog and take you back to blog_detail.html of the blog added.
    def get_absolute_url(self):
        return reverse('blog_detail', args=(str(self.id)))  #self.id is used to take you to the detailview of current new blog created