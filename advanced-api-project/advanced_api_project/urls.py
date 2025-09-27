from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

