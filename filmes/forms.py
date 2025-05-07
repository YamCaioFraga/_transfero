from django import forms #importa o modulo dos formulários do django.
from sistema.models import Filme 

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme  #Define qual é o model que o form representa.
        fields = ['nome_do_filme','ano_de_lancamento','estudio','genero','sinopse',]    