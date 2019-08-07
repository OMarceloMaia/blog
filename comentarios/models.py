from django.db import models

# Create your models here.

class Comentarios(models.Model):
    comentarios = models.TextField(verbose_name='comentarios')
    posts = models.ForeignKey("posts.Post", verbose_name='posts',on_delete=models.CASCADE)

    
    