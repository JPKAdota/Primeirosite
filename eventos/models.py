from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):

    nome = models.CharField('Nome', max_length=50)
    descricao= models.TextField('Descrição', blank=True)
    slug = models.SlugField('Identificador', max_length=50)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['nome']

class Evento(models.Model):

    nome = models.CharField('Nome', max_length=50)
    categoria = models.ForeignKey(Categoria, models.CASCADE)
    descricao= models.TextField('Descrição', blank=True)
    data = models.DateField('Data do Evento', null=True, blank=True)
    publicado = models.BooleanField ('Publicado', default=False)
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def save(self, *args, **kwargs):
        # Verifica se já existem 4 eventos com a mesma categoria
        eventos_da_categoria = Evento.objects.filter(categoria=self.categoria)
        if self.pk is None and eventos_da_categoria.count() >= 4:
            raise ValidationError("Não é possível adicionar mais do que 4 eventos para a mesma categoria.")
        
        super().save(*args, **kwargs)