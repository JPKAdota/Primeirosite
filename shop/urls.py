
from django.contrib import admin
from django.urls import path
from base.views import loja
from base.views import inscrever

urlpatterns = [
    path('inscrever/', inscrever, name='inscrever'),
    path('', loja, name='inicio'),
    path('admin/', admin.site.urls),
]
