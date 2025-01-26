from django.urls import path
from .views import VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView, VentaDeleteView

urlpatterns = [
    path('', VentaListView.as_view(), name='venta_list'),
    path('tienda/<int:pk>/', VentaDetailView.as_view(), name='venta_detail'),
    path('tienda/new/', VentaCreateView.as_view(), name='venta_new'),
    path('tienda/<int:pk>update/', VentaUpdateView.as_view(), name='venta_update'),
    path('tienda/<int:pk>/delete/', VentaDeleteView.as_view(), name='venta_delete'),
]