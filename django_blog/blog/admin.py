# blog/admin.py
from django.contrib import admin
from .models import Post, Profile, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'published_date', 'author', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author__username', 'content')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
