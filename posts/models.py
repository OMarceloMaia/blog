from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey("users.User", verbose_name='autor',on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='texto')
    created_at = models.DateTimeField(auto_now_add=True)
    categorias = models.ForeignKey("categorias.Categorias", verbose_name='categorias', on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f'Post {self.pk} | Author {self.autor} | Created at {self.created_at}'

    

