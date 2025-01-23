from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts
from django.shortcuts import get_object_or_404


class PostListView(ListView):
    model = Posts
    template_name = 'Feed/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Posts
    template_name = 'Feed/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(CreateView):
    model = Posts
    template_name = 'Feed/post_form.html'
    fields = ['title', 'description', 'link', 'image']
    success_url = reverse_lazy('post_list')
    
class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'Feed/post_form.html'
    fields = ['title', 'description', 'link', 'image']
    
class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'Feed/post_delete.html'
    success_url = reverse_lazy('post_list')


