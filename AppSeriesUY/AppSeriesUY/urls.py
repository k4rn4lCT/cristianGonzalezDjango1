from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SeriesUY.urls')),
    path('Feed/',include('Feed.urls')),
    path('Tienda/',include('Tienda.urls')),
]
