from django.urls import path
from categorias.views import CategoriaListView, CategoriaCreateView

app_name = 'categorias'

urlpatterns = [
    path('categoria',CategoriaListView.as_view(),name='list_categoria'),
    path('addcategoria',CategoriaCreateView.as_view(),name='add_categoria'),
]