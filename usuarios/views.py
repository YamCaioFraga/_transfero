from django.shortcuts import render, redirect
from sistema.models import Usuário
from usuarios.forms import UsuarioForm

# Create your views here.

def login(request):
    return render(
        request, 
        'usuario/login.html'
    )

def criarUsuario(request):
    # Verificar se a requisição será do tipo GET ou POST.
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)  
        # Será criado um objeto Usuario(model) com os dados enviados
        # post -> são os campos do forms (nome, sobrenome) preenchidos.
        # files -> Contém os módulos(arquivos) e ou as imagens.
        if form.is_valid(): # Se os dados forem validos, são salvos no BD. (Validação dos formularios)
            form.save()
            return redirect('usuario/login')

    else:
        # Se a requisição for do GET, exibir o formulário de cadastro.
        form = UsuarioForm()
    return render(
        request,
        'usuario/cadastrar.html',
        {'form': form} 
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