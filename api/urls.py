from django.urls import path
from api.views import categorias, adicionar_categorias,eventos

app_name ='api'

urlpatterns=[
    path ('categorias/', categorias, name='categorias'),
    path ('adicionar_categorias/', adicionar_categorias, name='adicionar_categorias'),
    path ('eventos', eventos, name='eventos')
]