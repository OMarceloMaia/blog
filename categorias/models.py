from django.db import models

# Create your models here.

class Categorias(models.Model):
    categorias = models.TextField(verbose_name='categorias', max_length=30)
    def __str__(self):
        return f'{self.categorias}'

    


