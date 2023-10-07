from django.shortcuts import render
from base.models import Contato
from base.forms import InscreverForm

def loja(request):
    return render(request, 'loja.html')
def inscrever(request):
    sucesso= False
    if request.method == 'GET':
        form = InscreverForm()
    else:
        form = InscreverForm(request.POST or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            data = form.cleaned_data['data']
            observacao = form.cleaned_data['observacao']
            sucesso = True
            Contato.objects.create(nome=nome, telefone=telefone, observacao=observacao, data=data)
    contexto = {
        'telefone': '(99) 9 9999-9999',
        'responsável': 'Maria da Silve Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'inscrever.html', contexto)


def loja (request):
    dados = []
    dados.append (
        {
            'titulo': 'Ttulo Legal 1',
            'categoria': 'Categoria 1',
            'data': '01/01/1989',
        },
    )
    dados.append(
        {
            'titulo': 'Ttulo Legal 2',
            'categoria': 'Categoria 2',
            'data': '13/01/1987',
        },
    )
    contexto = {
        'dados': dados
    }
    return render(request, 'loja.html', contexto)
