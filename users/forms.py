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
            # 'username': forms.TextInput(attrs={'class': 'form-control'}),
            # 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            # 'gender': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            # 'img': forms.FileInput(attrs={'class': 'form-control'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class EditUserForm(UserChangeForm):
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
            'password',
        )
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
