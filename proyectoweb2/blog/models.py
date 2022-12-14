from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        ordering=['nombre']
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50,null=False)
    Contenido=models.CharField(max_length=100,null=False)
    imagen = models.ImageField(upload_to='blog',null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        ordering=['titulo']
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.titulo

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    idioma=models.CharField(max_length=50,null=False)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='pais'
        verbose_name_plural='paises'
        ordering=['nombre']
    #para que nos devuelta el titulo del servicio
    #creacion de un self
    def __str__(self):
        return self.nombre