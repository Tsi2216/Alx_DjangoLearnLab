from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]