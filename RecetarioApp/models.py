from django.db import models
from datetime import date
from django.contrib.auth.models import User



categorias = (('POS', 'Postre'),('CEN', 'Cena'),)


class Pais(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/paises/%s/%s" % (self.nombre, filename)
        return ruta

    nombre = models.CharField(max_length=40, unique=True)
    bandera = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre



class Usuario(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/avatares/%s/%s" % (self.user.username, filename)
        return ruta

    user = models.OneToOneField(User)
    puntos = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.user.email


class Categoria(models.Model):
    
    nombre = models.CharField(max_length=60, blank=False, null=False, unique=True) 
    descripcion = models.TextField(max_length=120, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.nombre
        
        
class Ingrediente(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/ingredientes/%s/%s" % (self.nombre, filename)
        return ruta

    nombre  = models.CharField(max_length=100, unique=True)
    foto    = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre;



class Receta(models.Model):

    def url(self, filename):
        ruta = "MultimediaData/recetas/%s/%s" % (self.nombre, filename)
        return ruta

    nombre          = models.CharField(max_length=100, blank=False, null=False, unique=True)
    popularidad     = models.IntegerField(default=0)
    ingredientes    = models.ManyToManyField('Ingrediente', blank=False, null=False)
    descripcion     = models.TextField(max_length=500, blank=False, null=False)
    esVIP           = models.BooleanField(default=False, null=False)
    esDelDia        = models.BooleanField(default=False, null=False)
    fecha           = models.DateField(default=date.today(), blank=False, null=False)
    pais            = models.ForeignKey('Pais')
    categoria       = models.ManyToManyField('Categoria', blank=False, null=False)
    foto            = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre;



