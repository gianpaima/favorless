# Create your models here.
from django.contrib.auth.models import User
from django.db import models
#TipoProgramas:Comedia,Accion,Noticias,Reality,Deportes
class TipoPrograma(models.Model):
	titulo = models.CharField(max_length=60)

	def __unicode__(self):
		return self.titulo

#Ejemplo:Panorama, FA, Yo soy
class Programa(models.Model):
	nombre = models.CharField(max_length=60)
	fecha_creacion = models.DateField()
	hora_inicio_programa = models.TimeField()
	hora_fin_programa = models.TimeField()
	canal_programa = models.CharField(max_length=15)
	#Estado:Disponible,Cancelado,Break
	estados_todos = (('Di', 'Disponible'), ('Br', 'Break'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Di')
	logo = models.ImageField(upload_to='fotos/',blank=True,null=True)
	#LLave Foranea Tipo_Programa
	tipo_programa_id=models.ForeignKey(TipoPrograma)
	def __unicode__(self):
		return self.nombre

#Integrantes de los programas 
class Integrante(models.Model):
	nombres = models.CharField(max_length=60) 
	apellido_paterno = models.CharField(max_length=60)
	apellido_materno = models.CharField(max_length=60)
	foto_a = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_b = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_c = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_d = models.ImageField(upload_to='fotos/',blank=True,null=True)
	foto_e = models.ImageField(upload_to='fotos/',blank=True,null=True)
	programa_id = models.ForeignKey(Programa)


User.add_to_class('foto', models.ImageField(upload_to='fotos/',blank=True,null=True,default="fotos/default.png"))
User.add_to_class('nombreCompleto', models.CharField(max_length=20))