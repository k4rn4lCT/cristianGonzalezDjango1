from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ventas
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class VentaListView(LoginRequiredMixin,ListView):
    model = Ventas
    template_name = 'Tienda/venta_list.html'
    context_object_name = 'ventas'
    
class VentaDetailView(LoginRequiredMixin,DetailView):
    model = Ventas
    template_name = 'Tienda/venta_detail.html'
    context_object_name = 'venta'
    
class VentaCreateView(LoginRequiredMixin,CreateView):
    model = Ventas
    template_name = 'Tienda/venta_form.html'
    fields = ['nombre', 'descripcion', 'link', 'image']
    success_url = reverse_lazy('venta_list')
    
class VentaUpdateView(LoginRequiredMixin,UpdateView):
    model = Ventas
    template_name = 'Tienda/venta_form.html'
    fields = ['nombre', 'descripcion', 'link', 'image']
    
class VentaDeleteView(LoginRequiredMixin,DeleteView):
    model = Ventas
    template_name = 'Tienda/venta_delete.html'
    success_url = reverse_lazy('venta_list')


