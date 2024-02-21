import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from eventos.models import Categoria, Evento

@api_view()
def categorias(request):
    consulta = Categoria.objects.all()
    dados = []
    for categoria in consulta:
        dado = {
            'id': categoria.id,
            'nome': categoria.nome,
            'slug': categoria.slug,
        }
        dados.append(dado)
    return Response(json.dumps(dados))

@api_view(http_method_names=['POST'])
def adicionar_categorias(request):
    nome =  request.POST['nome']
    slug = request.POST['slug']
    categoria = Categoria.objects.create(nome=nome, slug=slug)
    dado = {
            'id': categoria.id,
            'nome': categoria.nome,
            'slug': categoria.slug,
        }
    return Response( dado)

@api_view()
def eventos(request):
    consulta = Evento.objects.all()
    dados = []
    for evento in consulta:
        dado = {
            'nome': evento.nome,
            'categoria': {
                'id':evento.categoria.id,
                'nome': evento.categoria.nome,
                'slug': evento.categoria.slug,
            },
            'data':evento.data,
            'descricao': evento.descricao,
            'criado_em': evento.criado_em,
        }
        dados.append(dado)
    return Response(dados)


