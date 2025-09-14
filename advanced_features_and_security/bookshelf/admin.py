from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, Review, CustomUser

class CustomUserAdmin(UserAdmin):
    # Add the custom fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Add the custom fields to the list_display
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Review)