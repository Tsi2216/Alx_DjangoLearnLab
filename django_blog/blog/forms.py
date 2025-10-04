# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class PostForm(forms.ModelForm):
    # tags input as comma-separated string
    tags = forms.CharField(required=False, help_text='Comma-separated tags (e.g. django, python)')

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'status', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your content...'}),
        }

    def __init__(self, *args, **kwargs):
        # if editing, populate tags field with current tags
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['tags'].initial = ', '.join([t.name for t in instance.tags.all()])

    def clean_tags(self):
        raw = self.cleaned_data.get('tags', '')
        # normalize, remove empty names, lower/strip duplicates
        names = [n.strip() for n in raw.split(',') if n.strip()]
        # preserve case but dedupe by lower
        unique = []
        seen = set()
        for n in names:
            key = n.lower()
            if key not in seen:
                seen.add(key)
                unique.append(n)
        return unique  # return list of tag names

    def save(self, commit=True):
        # Save post first (without tags), then attach tags
        tag_names = self.cleaned_data.pop('tags', [])
        post = super().save(commit=commit)
        # create/get Tag objects and set M2M
        tag_objs = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag_obj)
        post.tags.set(tag_objs)
        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) > 2000:
            raise forms.ValidationError("Comment is too long (max 2000 characters).")
        return content
