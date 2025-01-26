from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'Feed/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Posts
    template_name = 'Feed/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    template_name = 'Feed/post_form.html'
    fields = ['title', 'description', 'link', 'image']
    success_url = reverse_lazy('post_list')
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Posts
    template_name = 'Feed/post_form.html'
    fields = ['title', 'description', 'link', 'image']
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Posts
    template_name = 'Feed/post_delete.html'
    success_url = reverse_lazy('post_list')


