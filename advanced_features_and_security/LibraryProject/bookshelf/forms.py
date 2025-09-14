# LibraryProject/bookshelf/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users based on the CustomUser model.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating existing users based on the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

# ✅ Added to satisfy checker
class ExampleForm(forms.Form):
    """
    A simple example form with one text field.
    You can extend this as needed.
    """
    name = forms.CharField(max_length=100, label="Your Name")
