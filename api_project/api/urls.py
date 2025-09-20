from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet for full CRUD
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView (optional, still works)
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for CRUD operations
    path('', include(router.urls)),

    # Endpoint to obtain auth token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

