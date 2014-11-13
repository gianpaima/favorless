from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
# Usuario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Formularios
from forms import FormRegistrarUsuario,FormInciarSesion
#Modelos
from models import *
# Create your views here.
def home(request):
	template='principal.html' 
	form_registrar_usuario = FormRegistrarUsuario()
	form_iniciar_sesion = FormInciarSesion()
	print "hola mundp"
	return render_to_response(template,{"form_registrar_usuario":form_registrar_usuario,"form_iniciar_sesion":form_iniciar_sesion},context_instance=RequestContext(request))
