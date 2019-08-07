from posts.models import Post
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.views import generic

from django.urls import reverse_lazy
from posts.forms import PostCreateForm

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
    ordering = ['-created_at',] #ordem que ele pega vai ser invertida

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    # context_object_name = 'addPosts'
    template_name = 'posts/addposts.html'
    success_url = reverse_lazy('posts:list_posts')

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ['autor', 'texto']
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:list_posts')

class PostDeleteView(generic.DeleteView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:list_posts')

