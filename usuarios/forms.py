from django import forms #importa o modulo dos formulários do django.
from sistema.models import Usuário 

class UsuarioForm(forms.ModelForm):
    model = Usuário #Define qual é o model que o form representa.
    fields = ['nome','sobrenome','cpf','telefone','email','endereco','imagem',] #São os campos que serão exibidos no form (HTML).
