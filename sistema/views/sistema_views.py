from django.shortcuts import render
from sistema.models import Usuário

# Aqui irão ficar todas as views(controladores) ref ao sistema
# A Função index informa o que vai acontecer quando ela for chamada.

def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )

def listarUsuarios(request):
    usuarios = Usuário.objects.all()

    context = {
        'usuarios': usuarios 
    }

    return render(
        request,
        'usuarios/listar.html',
        context,
    )

