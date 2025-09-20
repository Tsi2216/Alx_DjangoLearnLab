from django.urls import path
from .views import BookList, home

urlpatterns = [
    path('', home, name='home'),           # root path
    path('books/', BookList.as_view(), name='book-list'),
]
