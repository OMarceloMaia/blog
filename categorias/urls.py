from django.urls import path
from categorias.views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

app_name = 'categorias'

urlpatterns = [
    path('categoria',CategoriaListView.as_view(),name='list_categoria'),
    path('addcategoria',CategoriaCreateView.as_view(),name='add_categoria'),
    path('alterar/<int:pk>', CategoriaUpdateView.as_view(),name='edit_categoria'),
    path('deletar/<int:pk>', CategoriaDeleteView.as_view(),name='del_categoria'),

]