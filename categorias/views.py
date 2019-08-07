from categorias.models import Categorias
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.views import generic

from django.urls import reverse_lazy
from categorias.forms import CategoriaCreateForm

# Create your views here.

class CategoriaListView(ListView):
    model = Categorias
    context_object_name = 'categoria'
    #template_name = 'categoria/addcategoria.html'
    #ordering = ['-created_at',]

class CategoriaCreateView(CreateView):
    model = Categorias
    form_class = CategoriaCreateForm
    context_object_name = 'addCategoria'
    template_name = 'categoria/addcategoria.html'
    success_url = reverse_lazy('posts:add_post')

class CategoriaUpdateView(generic.UpdateView):
    model = Categorias
    fields = ['categorias']
    template_name = 'categoria/edit.html'
    success_url = reverse_lazy('posts:list_posts')

class CategoriaDeleteView(generic.DeleteView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = 'categoria/delete.html'
    success_url = reverse_lazy('posts:list_posts')