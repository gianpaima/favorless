from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

# Create your models here.
class MyAppModel(models.Model):
    class Meta:
        app_label = 'votos'
        abstract = True

class Question(MyAppModel):
	#ListFields are very useful when used together with Embedded Models to store lists of sub-entities to model 1-to-n relationships:
	#comments = ListField(EmbeddedModelField('Comment'))
	asking = models.CharField(max_length=160)
	fecha_ask = models.DateTimeField(auto_now=True)
	participantes = ListField(EmbeddedModelField('Participation'))
	usuario_votar = ListField(EmbeddedModelField('User_Vote'))

class Participation(MyAppModel):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	estados_todos = (('Di', 'Disponible'), ('Br', 'Break'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Di')

class User_Vote(MyAppModel):
	nombre_completo = models.CharField(max_length=100)
	vote = models.CharField(max_length=2)
	fecha_vote = models.DateTimeField(auto_now=True)
	estados_todos = (('Ac', 'Activo'), ('Re', 'Reportado'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Ac')
	#estado activo
