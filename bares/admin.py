# -*- encoding: utf-8 -*-
from django.contrib import admin
from bares.models import Bares, Tapas

#Añadimos para mejorar la interfaz de administracion
class BaresAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('n_bar',)}
# Actualizado el registro
admin.site.register(Bares, BaresAdmin)
admin.site.register(Tapas)