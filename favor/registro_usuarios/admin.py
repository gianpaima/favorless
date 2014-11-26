from django.contrib import admin
from models import Categoria, Programa, Integrante

class ProgramaAdmin(admin.ModelAdmin):
	list_display =('nombre', 'fecha_creacion','hora_inicio_programa','hora_fin_programa','canal_programa','estado','logo')

class IntegranteAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellido_paterno','apellido_materno','programa','foto_a','foto_b','foto_c','foto_d','foto_e')


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Programa,ProgramaAdmin)
admin.site.register(Integrante,IntegranteAdmin)
