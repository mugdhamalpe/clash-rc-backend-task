from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields

OPTIONS = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # firstname = forms.CharField(max_length=200)
    # lasttname = forms.CharField(max_length=200)
    # gender = forms.ChoiceField(choices = OPTIONS)
    # phonenumber = forms.IntegerField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


