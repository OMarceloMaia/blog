from django import forms
from categorias.models import Categorias

class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['categorias']  