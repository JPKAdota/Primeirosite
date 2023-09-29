from django.shortcuts import render

from base.forms import InscreverForm

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

def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['nome'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['observacao'])
        print(form.cleaned_data['data'])
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)