from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('countrycases/', include('countrycases.urls')),
    path('admin/', admin.site.urls),
]
