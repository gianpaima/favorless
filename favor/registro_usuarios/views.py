from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
# Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Formularios
from forms import FormRegistrarUsuario, FormInciarSesion
#Modelos
from models import *
# Create your views here.


def home(request):
    template='inicio.html'
    form_registrar_usuario = FormRegistrarUsuario()
    form_iniciar_sesion = FormInciarSesion()
    return render_to_response(template,{"form_registrar_usuario":form_registrar_usuario,"form_iniciar_sesion":form_iniciar_sesion},context_instance=RequestContext(request))


def iniciarSesion(request):
    if not request.user.is_authenticated():
        if request.method == "POST":
            iniciar_sesion = FormInciarSesion(request.POST)
            if iniciar_sesion.is_valid():
                email = iniciar_sesion.cleaned_data['iniciar_input_email']
                clave = iniciar_sesion.cleaned_data['iniciar_input_password']
                acceso = authenticate(username=email,password=clave)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        return HttpResponseRedirect('/principal')
                    else:
                        iniciar_sesion = FormInciarSesion(request.POST)
                        return render_to_response('ingresoSesion.html',{'form_iniciar_sesion':iniciar_sesion,'error':'Su cuenta ha sido desactivada,por violar los derechos de uso'},context_instance = RequestContext(request))
                else:
                    iniciar_sesion = FormInciarSesion(request.POST)
                    return render_to_response('ingresoSesion.html',{'form_iniciar_sesion':iniciar_sesion,'error':'Por favor Ingrese Correctamente su usuario o password'},context_instance=RequestContext(request))
            else:
                template = "ingresoSesion.html"
                iniciar_sesion = FormInciarSesion(request.POST)
                return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion},context_instance=RequestContext(request))
        else:
            template = "ingresoSesion.html"
            iniciar_sesion = FormInciarSesion(request.POST)
            return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/principal")


def registrarUsuario(request):
    if not request.user.is_authenticated():
        #Aca no vamos a validar el metodo post o get por que esto sirve solo para capturar datos, puesto por primera vez y ponerlos en el otro html...Menos la contrasena
        registrar_usuario = FormRegistrarUsuario(request.REQUEST)
        return render_to_response('registroUsuario.html',{"form_registrar_usuario":registrar_usuario},context_instance=RequestContext(request))
    else:
        #aca falta ver si el usuario...esta desactivado...o  reportado
        return HttpResponseRedirect("/")


def principal(request):
    template = "principal.html"
    return render_to_response(template,context_instance=RequestContext(request))


@login_required(login_url='/login')
def cerrarSesion(request):
    logout(request)
    return  HttpResponseRedirect('/')

Programa




def preferencias(request):
    preferencias_todas = Programa.objects.all()
    categoria_todas = Categoria.objects.all()
    template = "inicio2.html"
    return render_to_response(template, {"preferencia_dato":preferencias_todas , "categoria_dato":categoria_todas},context_instance=RequestContext(request))


"""
    def elegir_preferencias(request,valor_preferencia):
        if valor_preferencia == "todos":
            preferencias_todos = Programa.objects.all()
    """    


    
