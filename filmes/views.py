from django.shortcuts import render, redirect

from filmes.forms import FilmeForm

# Create your views here.

def login(request):
    return render(
        request, 
        'cadastrar.html'
    )

def cadastrarFilme(request):
    # Verificar se a requisição será do tipo GET ou POST.
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)  
        # Será criado um objeto Usuario(model) com os dados enviados
        # post -> são os campos do forms (nome, sobrenome) preenchidos.
        # files -> Contém os módulos(arquivos) e ou as imagens.
        if form.is_valid(): # Se os dados forem validos, são salvos no BD. (Validação dos formularios)
            form.save()
            return redirect('/cadastrarfilme')

    else:   
        # Se a requisição for do GET, exibir o formulário de cadastro.
        form = FilmeForm()
    return render(
        request,
        'cadastrar.html',
        {'form': form} 
    )