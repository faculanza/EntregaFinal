from django.db import models
from django.contrib.auth.models import User

#USUARIOS
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to="imgUsr", null=True, blank=True)
    email = models.EmailField()

#BLOG
class Blogs(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    resumen = models.TextField()
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="imgBlogs", null=True, blank=True)
    idusuario = models.IntegerField()
    fecha = models.DateField()

#COMENTARIOS (estos serían los comentarios en los blogs)
class Comentarios(models.Model):
    comentario = models.TextField()
    idusuario = models.IntegerField()
    idblog = models.IntegerField()
    fecha = models.DateField()

#Para la app de mensajeria
class Mensajes(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    mensaje = models.TextField()
    idautor = models.IntegerField()
    iddestinatario = models.IntegerField()

