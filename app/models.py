from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __string__ (self):
        print(self.nombre)
        return self.nombre

class Noticia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='app/img/',help_text="Seleccione una imagen para mostrar")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='Noticia')

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()

    def __str__(self):
        return self.titulo + ' | Hecho Por ' + str(self.autor)


class Comentarios(models.Model):
    noticia = models.ForeignKey('Noticia',related_name='Comentarios', on_delete=models.CASCADE)
    autor =  models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)



#Para usuario
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default="Etiqueta de comentario")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):

        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post')
