from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'gender',
            'location',
            'dob',
            'img',
            'password1',
            'password2',
        )
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'mobile',
            'gender',
            'location',
            'dob',
            'img',
            'password',
        )
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
