from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
# Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Formularios
from forms import FormRegistrarUsuario, FormInciarSesion
#Modelos
from models import *
from ValidarUsuarios import ValidarUsuario
import json
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


def registrarUsuarioInicio(request):
    if not request.user.is_authenticated():
        #Aca no vamos a validar el metodo post o get por que esto sirve solo para capturar datos, puesto por primera vez y ponerlos en el otro html...Menos la contrasena
        registrar_usuario = FormRegistrarUsuario(request.REQUEST)
        return render_to_response('registroUsuario.html',{"form_registrar_usuario":registrar_usuario},context_instance=RequestContext(request))
    else:
        #aca falta ver si el usuario...esta desactivado...o  reportado
        return HttpResponseRedirect("/")

def registrarUsuarioFin(request):

    if request.method== 'POST' and not request.user.is_authenticated():
        print request.POST
        print "++++++*****"
        password = request.POST.get('registro_input_password','')
        nombre = request.POST.get('registro_input_nombre_completo','')
        usuario = request.POST.get('registro_input_usuario','')
        email = request.POST.get('registro_input_email','')
        kalena = ValidarUsuario().validarTodos(nombre, email, password, usuario)
        print kalena
        print "la twinem"
        #VNOmbre...VEmail..VPassword...VUsername
        print kalena.get('validoE')
        if False and kalena.get('validoN') == "0" and kalena.get('validoE') == "0" and kalena.get('validoP') == "0" and kalena.get('validoU') == "0": 
            try:
                usuario_create = User.objects.create_user(username= usuario, email= email, password= password, nombreCompleto= nombre)
                print "Usuario Creado"
                print usuario_create
                a=usuario_create.save()
                print "Usuario Guardado"
                print a
                print "email"
                print email
                print "password"
                print password
                user = auth.authenticate(username = email, password= password)
                print "Usuario Autenticado"
                print user
                print "QUE PASA!!!"

                if user is not None and user.is_active:
                    auth.login(request,user)
                else:
                    print "Ocurrio un Error"
                    return HttpResponse("Algo paso mal!")
            except:
                print "Hubo un error en la creacion del usuario"
                print "Se tiene que crear un diccionario que direccione el error"
                raise
            else:
                return HttpResponse("Se creo el usuario y logueo sin ningun error! Felicitaciones mi amigo!")

        else:
            #errores = {}
         #   errores ={'validoN':'Que haces'}
          #  for clave, valor in kalena.iteritems():
           #    if valor == "0":
            #        errores[clave] = valor
             #   elif valor == "1":
              #      errores[clave]=valor
              #  elif valor == "2":
               #     errores[clave] = valor
               # else:
                #    errores[clave] =valor
            #validoN-validoE-validoP-validoU    
            print "Llego a errores"
            print kalena
           # print kalena = {'validoN':'0'}
            print "finish MIke"
            return render_to_response('registroUsuario.html',{"errorN":kalena.get('validoN'),"errorE":kalena.get('validoE'), "errorP":kalena.get('validoP'),"errorU":kalena.get('validoU')},context_instance=RequestContext(request))            
            #return HttpResponse("Ha ocurrido ciertos errores")




        #for candace in kalena.values():
        #Aca no vamos a validar el metodo post o get por que esto sirve solo para capturar datos, puesto por primera vez y ponerlos en el otro html...Menos la contrasena
        #registrar_usuario = FormRegistrarUsuario(request.REQUEST)
      #  return render_to_response('registroUsuario.html',{"form_registrar_usuario":"registrar_usuario"},context_instance=RequestContext(request))
    else:
        if request.method == 'GET':
            return HttpResponse("HOLA MUNDO")
        return HttpResponse("era por esto")
        #aca falta ver si el usuario...esta desactivado...o  reportado
        #return HttpResponseRedirect("/")


def principal(request):
    template = "principal.html"
    return render_to_response(template,context_instance=RequestContext(request))


def validar(request):
    data = request.REQUEST.get("tipo","").strip()
  #  print request.REQUEST.get("objetos")
   # datas = serializers.serialize('json', request.REQUEST.items())
    #print datas
    if data!="validarTodos":
        if data == "validarEmail":
            obj = request.REQUEST.get("objetos[email]",'')
            datos= ValidarUsuario().validarEmail(obj)
            #data = serializers.serialize('json',ValidarUsuario().validarEmail(obj))
            #Retornar de forma ajax, en el
            d = json.dumps(datos)
            print "T"
            print d
            print "FIN"
            return HttpResponse(d, content_type='application/json')
            #return HttpResponse(datos)
        elif data == "validarNombre":
            obj = request.REQUEST.get("objetos[nombre]",'')
            datos=ValidarUsuario().validarNombre(obj)
            print datos
            return   HttpResponse(json.dumps(datos), content_type='application/json')
        elif data == "validarPassword":
            obj = request.REQUEST.get("objetos[password]",'')
            datos=ValidarUsuario().validarPassword(obj)
            print datos
            return HttpResponse(json.dumps(datos), content_type='application/json')
        elif data == "validarUsername":
            obj = request.REQUEST.get("objetos[username]",'')
            datos=ValidarUsuario().validarUsername(obj)
            print datos
            return HttpResponse(json.dumps(datos), content_type='application/json')
        else:
            print "Error"
            pass
    else:
        print "hola"
    #js= serializers.serialize('json',data)
    """ds=json.dumps(data)
    print "dataPost"
    print data['tipo']
    print "json"
    print ds
    """
    #data= serializers.serialize('json',request);
    #url-> Validar
    #Data->Primera Parte:email or username or password or nombre
    #Data->Segunda Parte: Que opcion va a validar
    return HttpResponse("status=400")




@login_required(login_url='/login')
def cerrarSesion(request):
    logout(request)
    return  HttpResponseRedirect('/')

    
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



