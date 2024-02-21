
from django.contrib import admin
from django.urls import path, include
from base.views import loja
from base.views import inscrever
from eventos.views import evento

urlpatterns = [
    path('inscrever/', inscrever, name='inscrever'),
    path('', loja, name='inicio'),
    path('eventos/<int:id>/', evento, name='evento'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace= 'api')),
]
