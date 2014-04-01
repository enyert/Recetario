__author__ = 'enyert'

from django.contrib import admin
from RecetarioApp.models import *

class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

class RecetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receta, RecetaAdmin)
admin.site.register(Categoria, CategoriaAdmin)