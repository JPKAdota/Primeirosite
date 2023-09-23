from django.shortcuts import render

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

