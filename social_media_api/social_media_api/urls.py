from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),

    # Redirect root to /api/
    path('', RedirectView.as_view(url='/api/', permanent=False)),
]

