from django.urls import path
#from . import views
from .views import AddBlogView, BlogDetailView, DeleteBlogView, EditBlogView, HomeView
urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('Blog/<int:pk>', BlogDetailView.as_view(),name="blog_detail"),
    path('Add/Blog/',AddBlogView.as_view(), name = "add_blog"),
    path('Blog/<int:pk>/edit', EditBlogView.as_view(), name = "edit_blog"),
    path('Blog/<int:pk>/delete', DeleteBlogView.as_view(), name="delete_blog"),
]