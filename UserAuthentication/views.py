from UserAuthentication.forms import SignUpForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm  #built in form
    template_name = 'registration/signUp.html'
    success_url = reverse_lazy('login')
