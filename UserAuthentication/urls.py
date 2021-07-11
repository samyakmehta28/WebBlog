from django.urls import path
from .views import SignUpView
urlpatterns = [
    path('SignUp/',SignUpView.as_view(),name="SignUp"),
]