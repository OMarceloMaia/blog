from comentarios.models import Comentarios
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from comentarios.forms import ComentariosCreateForm

# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'list_comentarios'
    template_name = 'comentarios/comentarios.html'
    #ordering = ['-created_at',]

class ComentariosCreateView(LoginRequiredMixin, CreateView):
    model = Comentarios
    form_class = ComentariosCreateForm
    context_object_name = 'add_Comentarios'
    template_name = 'comentarios/addcomentarios.html'
    success_url = reverse_lazy('comentarios:list_comentarios')

class ComentariosUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comentarios
    fields = ['comentarios']
    template_name = 'comentarios/edit.html'
    success_url = reverse_lazy('comentarios:list_comentarios')

class ComentariosDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = 'comentarios/delete.html'
    success_url = reverse_lazy('comentarios:list_comentarios')