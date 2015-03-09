from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
#Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#Fin
from models import *
from django.db.models import Q
from django.contrib.sessions.models import Session

#MongoDb
from bson.objectid import ObjectId
from bson.errors import InvalidId
from django.utils import timezone


def home(request):
    template='votos.html'
    return render_to_response(template,{},context_instance=RequestContext(request))


##Codigos de las preguntas...
#"_id" : ObjectId("54f284cadb01c42582a63584")
#"_id" : ObjectId("54f284cadb01c42582a63585")
#"_id" : ObjectId("54f284cadb01c42582a63586")
##Codigos de las participantes....
#codigo:1
#codigo:2
##Posicion de las participantes...
#numero:1
#numero:2

#Pasos a votar
#1.Buscar id pregunta en Mongo
#2.Insertar numero en la imagen
 #2.1.Buscar si el usuario ya ha votado
 #2.2.Ver si el voto es el mismo y si estan en los parametros indicados...

@login_required(login_url='/login')
def votar(request):
	#"_id" : ObjectId("54fc839ddb01c4157c7bd794")
	id_q="54fc839ddb01c4157c7bd794"
	print id_q
	##preguntar si el usuario esta activo o no!!!
	if request.method== 'POST':
	##Necesita usuario y voto,opcion participante....
		participante_opcion = '1'
		usuario = 'static'
		now = timezone.now()
		try:
			pr = Question.objects.get(pk=ObjectId(id_q))
			if buscarparticipante(pr.participante,participante_opcion):
				if not pr.usuariovotar.has_key(usuario):
					try:
						pr.usuariovotar.update({ usuario:{'voto':participante_opcion,'fecha':now,'estado':'activo'}})
						pr.save()
						return HttpResponse('Se creo el e-voting...')
					except Exception, e:
						print e
						return HttpResponse('Hubo un error en la bd')
				else:
					#update
					opcion = pr.usuariovotar.get(usuario).get('voto')
					print opcion
					if participante_opcion != opcion :	
						try:
							pr.usuariovotar.get(usuario)['voto']=participante_opcion
							pr.save()
							return HttpResponse('Se Actualizo eel voto')
						except Exception, e:
							print e
							print "ERROR"
							return HttpResponse('Hubo un error en la bd')	
					#model.DoesNotExist, ValidationError,ValueError
					return HttpResponse('Se actualizo el voto')
			else:
				return HttpResponse("No existe esa opcion")
		except InvalidId, TypeError:
			return HttpResponse("No existe en la bd")
		except Exception, e:
			print e
			return HttpResponse("mal")
		return HttpResponse("Listo!!!!") 
	else:
		return HttpResponse("Tomate un tiempo")
	
def buscarparticipante(diccionario,opcion_participante):
	for i in diccionario.values():
		if i.get('opcion') == opcion_participante:
			return True
	return False

