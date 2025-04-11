from django.shortcuts import render

from sistema.models import Usuário



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