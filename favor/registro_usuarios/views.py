from django.shortcuts import render_to_response, render, redirect 
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



def registrarUsuario(request):

    if request.method== 'POST' and not request.user.is_authenticated():
        password = request.POST.get('registro_input_password','')
        nombre = request.POST.get('registro_input_nombre_completo','')
        usuario = request.POST.get('registro_input_usuario','')
        email = request.POST.get('registro_input_email','')
        unico = ValidarUsuario().validarTodos(nombre, email, password, usuario)
        #VNOmbre...VEmail..VPassword...VUsername
        if unico.get('validoN') == "0" and unico.get('validoE') == "0" and unico.get('validoP') == "0" and unico.get('validoU') == "0": 
            try:
                usuario_create = User.objects.create_user(username= usuario, email= email, password= password, nombreCompleto= nombre)
                a=usuario_create.save()
                user = auth.authenticate(username = email, password= password)
                
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
            registrar_usuario = FormRegistrarUsuario(request.POST)
            return render_to_response('registroUsuario.html',{"form_registrar_usuario":registrar_usuario,"errorN":unico.get('validoN'),"errorE":unico.get('validoE'), "errorP":unico.get('validoP'),"errorU":unico.get('validoU')},context_instance=RequestContext(request))
            #return redirect('/signup/', respuesta = request)            
            #return HttpResponse("Ha ocurrido ciertos errores")
        #Aca no vamos a validar el metodo post o get por que esto sirve solo para capturar datos, puesto por primera vez y ponerlos en el otro html...Menos la contrasena
        #registrar_usuario = FormRegistrarUsuario(request.REQUEST)
      #  return render_to_response('registroUsuario.html',{"form_registrar_usuario":"registrar_usuario"},context_instance=RequestContext(request))
    else:
        registrar_usuario = FormRegistrarUsuario()
        return render_to_response('registroUsuario.html',{"form_registrar_usuario":registrar_usuario},context_instance=RequestContext(request))
        #aca falta ver si el usuario...esta desactivado...o  reportado
        #return HttpResponseRedirect("/")

@login_required(login_url='/login')
def configuracionGeneral(request): 
    return HttpResponseRedirect("/settings/password/")


@login_required(login_url='/login')
def configuracionPassword(request):
    #Se debe de agregar la validacion, si el usuario, esta supendido 
    if request.method == 'POST':
        error = ""
        before = request.POST.get('u_input_pass_before','')
        now = request.POST.get('u_input_pass_now', '')
        again = request.POST.get('u_input_pass_again', '')

        if ValidarUsuario().passwordZero(before) and ValidarUsuario().passwordFirst(now) and ValidarUsuario().passwordSecond(now,again):
            try: 
                if request.user.check_password(before):
                    print request.user.set_password(now)
                    error = "Se actualizo tu contrasena"
                else:
                    error = "La contrasena que has ingresado es incorrecta. Por favor ingresa una contrasena diferente."
            except:
                error = "Ha ocurrido un fallo, vuelva a intentarlo!"
        else:
            if len(before) <6:
                if len(before) == 0:
                    error = "Debes ingresar tu contrasena actual para poder cambiarla."
                else:
                    error = "Tu contrasena actual debe ser mayor a 5 caracteres"
            else:
                if len(now) < 6:
                    if len(now) == 0:
                        error = "Debes introducir una nueva contrasena para poder cambiarla."
                    else:
                        error= "Tu nueva contrasena debe tener mas de 5 caracteres"   
                else:
                    if now != again:
                        error = "Tu nueva contrasena debe ser confirmada correctamente."
                    else:
                        error = "Ha ocurrido un error"
        return render_to_response('configuracion.html',{'error':error},context_instance=RequestContext(request))
    else:
        return render_to_response('configuracion.html',context_instance=RequestContext(request))


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
            return HttpResponse(d, content_type='application/json')
            #return HttpResponse(datos)
        elif data == "validarNombre":
            obj = request.REQUEST.get("objetos[nombre]",'')
            datos=ValidarUsuario().validarNombre(obj)
            return   HttpResponse(json.dumps(datos), content_type='application/json')
        elif data == "validarPassword":
            obj = request.REQUEST.get("objetos[password]",'')
            datos=ValidarUsuario().validarPassword(obj)
            return HttpResponse(json.dumps(datos), content_type='application/json')
        elif data == "validarUsername":
            obj = request.REQUEST.get("objetos[username]",'')
            datos=ValidarUsuario().validarUsername(obj)
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

@login_required(login_url='/login')
def preferencias(request):
    user_p = request.user.id
    print "---------------------------------------"
    print user_p
    print "--------------------------------------"
    print "------------------------------------"
    categoria_todas = Categoria.objects.all()
    preferencias = Preferencia.objects.filter(user = user_p)
    print "xD"
    #print preferencias.filter("programa")
    #programas_todas = Programa.objects.exclude(id=preferencias.iterator())
    programas_todas = Programa.objects.all().exclude(id__in=preferencias.values_list('programa', flat=True))
    template = "inicio2.html"
    return render_to_response(template, {"list_programa_pref":preferencias,"programas_dato":programas_todas , "categoria_dato":categoria_todas},context_instance=RequestContext(request))


def removepreference(request):
    if request.method == 'POST':

        id_post  = request.POST.get('id','')
        if (id_post.isdigit()):

            try:
                preferencia = Preferencia.objects.get(pk = id_post)
                preferencia.estado = False
                preferencia.save()
                return HttpResponse("la preferencia se ha actualiza")
            except:
                return HttpResponse("ha ocurrido un error")
        else:
            return HttpResponse( "el id No existe" )

    else:
        return HttpResponse ("Anda a casa estas borracho")


def addpreference(request):
    if request.method == 'POST':
        id_post  = request.POST.get('id','')

        if (id_post.isdigit()):

            if(Preferencia.objects.filter(pk=id_post).exists()):

                try:
                    preferencia = Preferencia.objects.get(pk = id_post)
                    preferencia.estado = True
                    preferencia.save()
                    return HttpResponse("la Preferencia Existe y solo cambiara el estado")
                except:
                    return HttpResponse("ha ocurrido un error")

            else:
                try:        
                    print "estoy cuando la preferenia no existe"
                    programa_p  = Programa.objects.get(pk = id_post)
                    #print programa_p
                    user_p = request.user
                    #print  user_p
                    p = Preferencia.objects.create(user = user_p, programa = programa_p)
                    p.save()
                    #print programa_p.nombre
                    return HttpResponse(id_post)
                except:
                    return HttpResponse("ha ocuurido un error")


        else:
            return HttpResponse( "No Existe" )

    else: 
        return HttpResponse("anda a casa estas borracho")

import json
def buscarPrograma(request):
    buscar = request.REQUEST.get('search',)
    if buscar:
        programa = Programa.objects.filter(nombre__icontains=buscar).values('id', 'nombre','logo')
        #values_list
        print programa 
        return HttpResponse(json.dumps(list(programa)), content_type="application/json")
    return HttpResponse("")



        





