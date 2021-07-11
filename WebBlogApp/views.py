from WebBlogApp.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import AddBlogForm,EditBlogForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
#   return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['date']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class AddBlogView(CreateView):
    model = Post
    form_class = AddBlogForm   # will use the forms.py AddBlogform to create a form on add_blog html
    template_name = 'add_blog.html'
    #fields = '__all__'    #shows all fields in model Post to the html add_blog

class EditBlogView(UpdateView):
    model = Post
    template_name = 'edit_blog.html'
    form_class = EditBlogForm
    #fields = ['title', 'title_tag', 'body']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home') #deletes and takes you back to home.