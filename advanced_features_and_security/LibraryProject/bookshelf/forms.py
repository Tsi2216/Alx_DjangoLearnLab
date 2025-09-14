# LibraryProject/bookshelf/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users based on the CustomUser model.
    Extends Django's built-in UserCreationForm.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating existing users based on the CustomUser model.
    Extends Django's built-in UserChangeForm.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
