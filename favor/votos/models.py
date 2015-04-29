#from django_mongodb_engine.storage import GridFSStorage
from django_mongodb_engine.fields import GridFSField

from django.db import models
#from django.contrib.contenttypes.models import ContentType
#from djangotoolbox import *
from djangotoolbox.fields import ListField, EmbeddedModelField,DictField
from django_mongodb_engine.contrib import MongoDBManager



#from mongoengine import *
"""
from django.db import models  
from django_mongodb_engine.mongodb.fields import EmbeddedModel  
from django_mongodb_engine.fields import ListField  
# Create your models here.
"""
"""
class MyAppModel(models.Model):
    class Meta:
        app_label = 'votos'
        abstract = True
"""
class Question(models.Model):
	#ListFields are very useful when used together with Embedded Models to store lists of sub-entities to model 1-to-n relationships:
	#comments = ListField(EmbeddedModelField('Comment'))
	objects = MongoDBManager()
	usuario_creador =models.CharField(max_length=200)
	asking = models.CharField(max_length=160)
	fecha_ask = models.DateTimeField(auto_now=True)
	versus = models.ImageField(upload_to='fusion/',blank=True,null=True)
	participante = ListField(DictField())
	usuariovotar = DictField()
	#usuariovotar = ListField(DictField())
	#Para buscar....por usuario y (categoria,integrante,programa)
	for_search_cip = models.CharField(max_length=200)
	for_search_user= models.TextField()
	for_result_vote= ListField(models.IntegerField())

#participante debe ser formado:
#{clave:valor}->{codigo:{opcion:numero,alias:username,estado:activo}}
#estados_todos = (('Di', 'Disponible'), ('Br', 'Break'),('Ca', 'Cancelado'),)	
#UsuarioVotar debe de ser formado:
#{clave:valor}->{username:{voto:opcion,fecha:datetime,estado:activo}}
#...
#{clave:valor}-->{llave:username,valor:{voto:opcion,fecha:datetime,estado:activo}}
#estados_todos = (('Ac', 'Activo'), ('Re', 'Reportado'),('Ca', 'Cancelado'),)

"""
class Participation(models.Model):
	#participantes 1-2-3-4-5-6
	codigo = models.CharField(max_length=2)
	opcion = models.CharField(max_length=2)
	alias = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	estados_todos = (('Di', 'Disponible'), ('Br', 'Break'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Di')


class UserVote(models.Model):
	nombre = models.CharField(max_length=100)
	vote = models.CharField(max_length=2)
	fecha_vote = models.DateTimeField(auto_now=True)
	estados_todos = (('Ac', 'Activo'), ('Re', 'Reportado'),('Ca', 'Cancelado'),)
	estado = models.CharField(max_length=2,
                                      choices=estados_todos,
                                      default='Ac')
	#estado activo

class Post(models.Model):
    usuario = ListField(DictField())
    comentario = DictField()
    valores = ListField(DictField())
    cristiano = ListField(DictField())	
"""