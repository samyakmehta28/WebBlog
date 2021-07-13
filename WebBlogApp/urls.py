from django.urls import path
#from . import views
from .views import AddBlogView, AddCategoryView, BlogDetailView, CategoryListView, DeleteBlogView, EditBlogView, HomeView, CategoryView
urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('Blog/<int:pk>', BlogDetailView.as_view(),name="blog_detail"),
    path('Add/Blog/',AddBlogView.as_view(), name = "add_blog"),
    path('Blog/<int:pk>/edit', EditBlogView.as_view(), name = "edit_blog"),
    path('Blog/<int:pk>/delete', DeleteBlogView.as_view(), name="delete_blog"),
    path('Add/category/',AddCategoryView.as_view(), name = "add_category"),
    path('category/<str:cat>/', CategoryView, name = "category"),
    path('category-list/', CategoryListView, name = "category_list"),
]
