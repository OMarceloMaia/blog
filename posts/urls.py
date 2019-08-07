from django.urls import path
from posts.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('posts',PostListView.as_view(),name='list_posts'),
    path('addposts', PostCreateView.as_view(),name='add_post'),
    path('posts/<int:pk>/alterar',PostUpdateView.as_view(),name='update_post'),
    path('posts/<int:pk>/deletar',PostDeleteView.as_view(),name='delete_post'),
]