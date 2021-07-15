from django import forms
from .models import Post, Category

choice = Category.objects.all().values_list('name','name')
choice_list = []
for item in choice:
    choice_list.append(item)


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        #widgets is used for styling the fields -> widgets is a dictionary
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your blog title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title tag for your blog '}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_name', 'type':'hidden'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'})
        }

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        #widgets is used for styling the fields -> widgets is a dictionary
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your blog title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title tag for your blog '}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content of your blog here'})
        }