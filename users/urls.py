from django.urls import path
from users.views import UserListView, UserLoginView, UserLogoutView, UserRegisterView

app_name = 'users'

urlpatterns = [
    path('list',UserListView.as_view(),name='list_users'),
    path('login', UserLoginView.as_view(),name='login_user'),
    path('sair', UserLogoutView.as_view(),name='logout_user' ),
    path('cadastro', UserRegisterView.as_view(),name="register_user")
]