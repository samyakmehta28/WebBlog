from WebBlogApp.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import AddBlogForm,EditBlogForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
#   return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        blog_likes = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = blog_likes.total_likes()
        cat_menu = Category.objects.all()
        
        liked = False
        if blog_likes.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

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

class AddCategoryView(CreateView):
    model = Category
    #form_class = AddBlogForm   # will use the forms.py AddBlogform to create a form on add_blog html
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cat):
    category_blog = Post.objects.filter(category=cat)
    return render(request, 'category.html', {'cat': cat, 'category_blog': category_blog})

def CategoryListView(request):
    cat_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_list': cat_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blog_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
