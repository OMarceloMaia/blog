from users.models import User
from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserCreateForm
from django.urls import reverse_lazy

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass

class UserRegisterView(generic.CreateView):
    model = User
    template_name = "users/cadastro.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('users:login_user')

class UserSobreView(generic.DetailView):
    model = User
    template_name = "users/sobre.html"
    context_object_name = 'users'
    success_url = reverse_lazy('users:login_user')




    
    
    