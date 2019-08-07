from django.urls import path
from comentarios.views import ComentariosListView, ComentariosCreateView, ComentariosUpdateView, ComentariosDeleteView

app_name = 'comentarios'

urlpatterns = [
    path('comentarios',ComentariosListView.as_view(),name='list_comentarios'),
    path('addcomentatios',ComentariosCreateView.as_view(),name='add_comentarios'),
    path('alterar/<int:pk>/comentario', ComentariosUpdateView.as_view(),name='edit_comentarios'),
    path('deletar/<int:pk>/comentario', ComentariosDeleteView.as_view(),name='del_comentarios')

]

