from django import forms

from instructor.models import User

from django.contrib.auth.forms import UserCreationForm


class StudentCreateForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","password1","password2","email"]

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()
    