from django.urls import path
from .views import admin_view
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]
