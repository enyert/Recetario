from django.db import models
from datetime import date
from django.contrib.auth.models import User



categorias = (('POS', 'Postre'),('CEN', 'Cena'),)


class Pais(models.Model):

    def url(self, filename):
        ruta = "media/paises/%s/%s" % (self.nombre, filename)

    nombre = models.CharField(max_length=40, unique=True)
    bandera = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre



class Usuario(models.Model):

    def url(self, filename):
        ruta = "media/avatares/%s/%s" % (self.user.username, filename)

    user = models.OneToOneField(User)
    puntos = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.user.email



class Ingrediente(models.Model):

    def url(self, filename):
        ruta = "media/ingredientes/%s/%s" % (self.nombre, filename)

    nombre  = models.CharField(max_length=100, unique=True)
    foto    = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre;



class Receta(models.Model):

    def url(self, filename):
        ruta = "media/recetas/%s/%s" % (self.nombre, filename)

    nombre          = models.CharField(max_length=100, blank=False, null=False, unique=True)
    popularidad     = models.IntegerField(default=0)
    ingredientes    = models.ManyToManyField('Ingrediente', blank=False, null=False)
    descripcion     = models.TextField(max_length=500, blank=False, null=False)
    esVIP           = models.BooleanField(default=False, null=False)
    esDelDia        = models.BooleanField(default=False, null=False)
    fecha           = models.DateField(default=date.today(), blank=False, null=False)
    pais            = models.ForeignKey('Pais')
    categoria       = models.CharField(max_length=3, choices=categorias)
    foto            = models.ImageField(upload_to=url, blank=True, null=True)

    def __unicode__(self):
        return self.nombre;



