from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
#Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#Fin
from models import *
from django.db.models import Q
from django.contrib.sessions.models import Session
from registro_usuarios.models import Integrante,Programa,Preferencia
#MongoDb
from bson.objectid import ObjectId
from bson.errors import InvalidId
from django.utils import timezone
import json
#transaction
from django.db import IntegrityError, transaction
#Imagenes
from PIL import Image
#Reduce search
import operator
from django.db.models import Q
#Errores
from registro_usuarios.views import Error404,Error500

def buscarPrograma(buscar,preferencia):
    if buscar:
        total= []
        try:
            if preferencia:
                programa = Programa.objects.filter(Q(nombre__icontains=buscar) | Q(nombre_abreviado__icontains=buscar)).exclude(id__in=preferencia).values('id', 'nombre','logo','tipo_programa')
            else:
                programa = Programa.objects.filter(Q(nombre__icontains=buscar) | Q(nombre_abreviado__icontains=buscar)).values('id', 'nombre','logo','tipo_programa')
            for ask in buscar.split():
                integrante = Integrante.objects.filter(Q(nombres__icontains = ask) | Q(apellido_paterno__icontains = ask) | Q(apellido_materno__icontains=ask)).values('id', 'nombres','apellido_paterno','apellido_materno','foto_a','programa_p')
            if programa and integrante:
                total = list(programa)
                total.extend(list(integrante))
            else:
                if programa:
                    total = list(programa)
                if integrante:
                    total.extend(list(integrante))
        except Exception, e:
            total = None
        return total
    else:
        return ""

    return HttpResponse("")

def resultados(request):
    search = request.REQUEST.get('q','').strip()
    lista=[]
    if search!= "":
        try:
            prefer = Preferencia.objects.filter(Q(user=request.user.id),Q(estado=True),(Q(programa__nombre__icontains=search) | Q(programa__nombre_abreviado__icontains=search))).values('id','slug','programa__nombre','programa',)
            if prefer:
                lista=lista_id_preferencia(prefer)
        except Exception, e:
            lista = None
        if lista != None:
            total = buscarPrograma(search,lista)
            lista = list(prefer)
            if total!= None and total != []:
                lista.extend(total)

        else:
            print "KILL retornar, vuelva a intentarlo otro dia"
    else:
        lista =""
<<<<<<< HEAD
<<<<<<< HEAD

    #print "LISTA CON PREFERENCIA o SIN preferencia"
=======
    
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
=======
    
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
    template ="buscarprogramas.html"
    return render_to_response(template,{'total':lista},context_instance=RequestContext(request))

def lista_id_preferencia(preferencia):
    lista = []
    for p in preferencia:
        lista.append(p.get('programa'))
        #lista.append(str(p.programa))
    return lista

def static_page(request,slug=''):
    a = existe_entidad(slug.split("-",1))
    template = "buscar.html"
    pre = None
    cip = None
    if a:
        if not hasattr(a, 'programa_p'):
            #Programa
            try:
                pre = Preferencia.objects.only('slug').get(user=request.user.id,programa=a.id,estado=True)
            except Exception, e:
                pre = None
                print e
            try:
                cip='-cat-'+str(a.tipo_programa.id)+'-pro-'+str(a.id)
            except Exception, e:
                print e
                cip=None
        else:
            #Integranteprincipal
            try:
                cip = '-cat-'+str(a.programa_p.tipo_programa.id)+'-pro-'+str(a.programa_p.id)
            except Exception, e:
                print "Error"
                cip = None
        if cip:
            try:
                cip = Question.objects.exclude(for_search_user__contains='-%s-' %(str(request.user.id))).filter(for_search_cip__icontains=cip)
            except Exception, e:
                print e
                cip =None

    elif a == []:
        #retornar error 404
        return Error404(request)
    #None    a pre cip
    return render_to_response(template,{'pagina':a,'gustar':pre,'total':cip},context_instance=RequestContext(request))


@login_required(login_url = '/login')
def misVotaciones(request):
    template = "principal.html"
    try:
        #questions = Question.objects.filter(for_search_user__contains = '-%s-'  %(str(request.user.id)))
        questions = Question.objects.filter(for_search_user__icontains = '-%s' %(str(request.user.id)))
    except Exception ,e :
        print e

    for pregunta in questions:
        pregunta.votos = pregunta.for_result_vote[0] + pregunta.for_result_vote[1]

    cuatro_preferencias = cuatroPrefe(request.user.id)
    return render_to_response(template,{'total':questions,'seguir':cuatro_preferencias},context_instance=RequestContext(request))






#gridfs = GridFSStorage()
#uploads = GridFSStorage(location='/uploads')
@login_required(login_url='/login')
def principal(request):
    template = "principal.html"
    total = []
    lista = lista_preferencia(request.user.id)
    if lista:
        #data.objects.filter(name__regex=r'(word1|word2|word3)')
        #You can do that using the regex search too, avoiding many Q expressions (which end up using that many where "and" clauses in the SQL, possibly dampening the performance), as follows:
        try:
            query = reduce(operator.or_, (Q(for_search_cip__contains = item) for item in lista ))
            total = Question.objects.exclude(for_search_user__contains='-%s-' %(str(request.user.id))).filter(query)
        except Exception, e:
            total = None
    elif lista == []:
        #total = Question.objects.values('usuariovotar').annotate(numero_pregunta=Count('usuariovotar')).order_by('-usuariovotar')
        try:
            total = Question.objects.exclude(for_search_user__contains='-%s-' %(str(request.user.id))).order_by('-usuariovotar')
            for pregunta in total:
                pregunta.votos = pregunta.for_result_vote[0] + pregunta.for_result_vote[1]
        except Exception, e:
            total = None

        #Listarle las preguntas mas votadas
    else:
        total = None

<<<<<<< HEAD
<<<<<<< HEAD


    print total
=======
    
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
=======
    
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
    # try:
    #     #aca esta el error
    #     preferido = Preferencia.objects.filter(user=request.user.id,estado=True).values('programa__tipo_programa__id','programa__id')
    #     cuatro_preferencias=[]
    #     gustar = []
    #     for dato in preferido:
    #         gustar.append(dato['programa__id'])
    #         if dato['programa__tipo_programa__id'] not in cuatro_preferencias:
    #             cuatro_preferencias.append(dato['programa__tipo_programa__id'])
    #     if cuatro_preferencias:
    #         try:
    #             cuatro_preferencias = Programa.objects.exclude(id__in=gustar).filter(tipo_programa__id__in=cuatro_preferencias).values('tipo_programa__id','nombre')[:4]
    #         except Exception, e:
    #             cuatro_preferencias = None
    #     else:
    #         try:
    #             cuatro_preferencias = Programa.objects.all()[:4]
    #         except Exception, e:
    #             cuatro_preferencias = None

    # except Exception, e:
    #     print e
    #     cuatro_preferencias = None
    cuatro_preferencias = cuatroPrefe(request.user.id)
<<<<<<< HEAD
<<<<<<< HEAD

    print cuatro_preferencias
=======
   
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
=======
   
>>>>>>> 2bc2816e6b793c716a17a0c694088f96361f57b4
    return render_to_response(template,{'total':total,'seguir':cuatro_preferencias},context_instance=RequestContext(request))

def cuatroPrefe(user_id):

    try:
        #aca esta el error
        preferido = Preferencia.objects.filter(user=user_id,estado=True).values('programa__tipo_programa__id','programa__id')
        cuatro_preferencias=[]
        gustar = []
        for dato in preferido:
            gustar.append(dato['programa__id'])
            if dato['programa__tipo_programa__id'] not in cuatro_preferencias:
                cuatro_preferencias.append(dato['programa__tipo_programa__id'])
        if cuatro_preferencias:
            try:
                cuatro_preferencias = Programa.objects.exclude(id__in=gustar).filter(tipo_programa__id__in=cuatro_preferencias).values('tipo_programa__id','nombre')[:4]
            except Exception, e:
                cuatro_preferencias = None
        else:
            try:
                cuatro_preferencias = Programa.objects.all()[:4]
            except Exception, e:
                cuatro_preferencias = None

    except Exception, e:
        print e
        cuatro_preferencias = None

    return cuatro_preferencias

#.----------------------------------------------------------------------------------

def lista_preferencia(id):
    try:
        preferencia = Preferencia.objects.filter(user=id, estado=True)
        total = []
        for pr in preferencia:
            total.append('-cat-%s-pro-%s-' %(str(pr.programa.tipo_programa.id), str(pr.programa.id)))
        return total
    except Exception, e:
        print e
        return None


def home(request):
    template='votos.html'
    return render_to_response(template,{},context_instance=RequestContext(request))

#Pasos a votar
#1.Buscar id pregunta en Mongo
#2.Insertar numero en la imagen
 #2.1.Buscar si el usuario ya ha votado
 #2.2.Ver si el voto es el mismo y si estan en los parametros indicados...

#@login_required(login_url='/login')
#ver lo de decoradores con nodejs

@transaction.atomic
def votar(request):
    if request.method== 'POST':
	#Necesita usuario y voto,opcion participante....
        usuario = fuente_user(request)
        if usuario:

            try:
                id_q = request.POST.get('question','')
                pr = Question.objects.get(pk=ObjectId(id_q))
                opcion = request.POST.get('opcion','')
                if buscarparticipante(pr.participante,opcion):
                    if not pr.usuariovotar.has_key(str(usuario.id)):
                        try:
                            with transaction.atomic():
                                now = timezone.now()
                                pr.usuariovotar.update({ str(usuario.id) :{'voto':opcion,'fecha':now,'estado':'activo'}})
                                #pr.usuariovotar.append({'clave':str(usuario.id),'valor':{'voto':opcion,'fecha':now,'estado':'activo'}})
                                #desde aca ver el result_vote


                                opc_actual = int(opcion)-1

                                pr.for_result_vote[opc_actual] +=1


                                if pr.for_search_user:
                                    pr.for_search_user +=  str(usuario.id) + '-'
                                else:
                                    pr.for_search_user += '-'+  str(usuario.id)+'-'
                                pr.save()

                                return HttpResponse(json.dumps(['1',pr.for_result_vote,id_q ]))
                        except IntegrityError:
                            print IntegrityError
                            return HttpResponse('0')
                    else:
                        #update
                        opcion_antes = pr.usuariovotar.get(str(usuario.id)).get('voto')
                        if opcion != opcion_antes :
                            try:
                                with transaction.atomic():
                                    pr.usuariovotar.get(str(usuario.id))['voto']=opcion
                                    opc_aux = int(opcion_antes)-1
                                    pr.for_result_vote[opc_aux] -= 1
                                    opc_actual = int(opcion)-1
                                    pr.for_result_vote[opc_actual] += 1
                                    #pr.for_result_vote[]
                                    pr.save()
                                    return HttpResponse(json.dumps(['1',pr.for_result_vote,id_q ]))
                           # except Exception, e:
                            except IntegrityError:
                                print IntegrityError
                                return HttpResponse('0')

                        else:
                            return HttpResponse(json.dumps(['2',pr.for_result_vote]))
                        #model.DoesNotExist, ValidationError,ValueError
                else:
                    return HttpResponse("0")
            except InvalidId, TypeError:
                return HttpResponse("0")
            except Exception, e:
                return HttpResponse("0")
        else:
            return HttpResponse('0')

    else:
		return HttpResponse("Tomate un tiempo")


def fuente_user(request):
    if request.user.is_authenticated():
            user = request.user
            return user
    else:
        if request.POST.get('sessionid'):
            try:
                session = Session.objects.get(session_key=request.POST.get('sessionid'))

                user_id = session.get_decoded().get('_auth_user_id')

                user = get_or_none(User,**{'id':user_id} )
                return user
            except Exception,e:
                print e
                return None
        return None


def buscarparticipante(lista,opcion_participante):
    for diccionario in lista:
        for i in diccionario.values():
          if i.get('opcion') == opcion_participante:
            return True
    return False

def versus(request):
    if request.method == "GET":

        template = "crearVersus.html"
        return render_to_response(template,context_instance=RequestContext(request))


def uniimg(img1,img2):
    #cargar las dos imagenes desde el directorio donde estoy ejecutando el Script
    # Abrir  img  1
    im1 = Image.open(img1)
    # Abir img 2
    im2 = Image.open(img2)
    # crear una imagen de Fondo que  contiene las dos imagenes
    salida  =  Image.new ("RGB", (640,480),(0,0,255)) # imagen de 640*480 de fondo blanco
    # redimensionar cada imagenpng para que ocupe el lugar indicado
    a = im1.resize((salida.size[0]/2 - 1, salida.size[1]))
    b = im2.resize((salida.size[0]/2 - 1, salida.size[1]))
    #Ahora copiar cada imagen a la imagen de salida
    salida.paste(a,(0,0))
    salida.paste(b,(a.size[0] + 2,0))
    #salida.save("prueba.jpg", "JPEG")
    return salida
    #salida.save("salida2.jpg",optimize=True)

def manjar_imagen_subida(i):
    import StringIO
    from PIL import Image,ImageOps
    #import os
    #Sfrom django.core.files import File
    image_str = ""
    for c in i.chunks():
        image_str += c
    imagenFile  = StringIO.StringIO(image_str)
    image = Image.open(imagenFile)
    return image

def fusion_imagen(img1,img2):
    try:
        q = unirlas(img1,img2)
    except Exception, e:
        print e
        return None
    return q

def unirlas(a,b):
    from PIL import Image
    import os
    from django.core.files import File
    salida = Image.new ("RGB", (640,480),(0,0,255))
    out1 = a.resize((salida.size[0]/2 - 1, salida.size[1]),Image.ANTIALIAS)
    out2 = b.resize((salida.size[0]/2 - 1, salida.size[1]),Image.ANTIALIAS)
    salida.paste(out1,(0,0))
    salida.paste(out2,(out1.size[0] + 2,0))

    filename = "sandro3.jpg"
    imagefile = open(os.path.join("c:", "/Users/GianCarlos/Documents/Nueva",filename), 'wb')
    salida.save(imagefile,"JPEG", quality=90)
    imagefile = open(os.path.join("c:", "/Users/GianCarlos/Documents/Nueva",filename), 'rb')

#    filename = "sandro3.jpg"
#    imagefile = open(os.path.join("/home/sandro/Escritorio/pruebasImagenesDj/",filename), 'w')
#    salida.save(imagefile,"JPEG", quality=90)
#    imagefile = open(os.path.join("/home/sandro/Escritorio/pruebasImagenesDj/",filename), 'r')
    content = File(imagefile)
    return content

def formar_participante(opc,modelo,numero):
    #{codigo:{opcion:numero,alias:username,estado:activo}}
    # p1 = {opc1:{'opcion':'1','alias':}}
    if len(opc)==2:
        #Es integrante
        return ({opc[0]+'-'+opc[1]:{'opcion': numero,'alias':'%s %s %s' %(modelo.nombres,modelo.apellido_paterno,modelo.apellido_materno),'estado':''}},'-cat-%s-pro-%s-int-%s-' %(modelo.programa_p.tipo_programa.id, modelo.programa_p.id,modelo.id) )
    else:
        #Es programa
        ##Si solo es 1
        #print "Viene"
        return ({str(modelo.id):{'opcion':numero,'alias':modelo.nombre,'estado':modelo.estado}}, '-cat-%s-pro-%s-int-0-' %(modelo.tipo_programa.id, modelo.id) )


def existe_entidad(*args):
    if len(*args) == 1:
        return get_or_none(Programa,**{'id':args[0][0]})
        #Entonces es programas
    elif len(*args)==2:
       # print get_or_none(Integrante,**{'id':args[0][0],'programa':args[0][1]})
        return get_or_none(Integrante,**{'id':args[0][0],'programa_p':args[0][1]})
        #Entonces es integrantes
    else:
        return None

def post_versus(request):
    if request.method == "POST":
        pregunta = request.POST.get('pregunta')
        opc1 = request.POST.get('opc1Id').split("-",1)
        opc2 = request.POST.get('opc2Id').split("-",1)
        img1=manjar_imagen_subida(request.FILES['file1'])
        img2= manjar_imagen_subida(request.FILES['file2'])
        """
        print "--------------"
        print request.FILES
        # print pregunta
        # print opc1
        print "img 1"
        print img1
        print "img 2"
        print img2
        print "Imagen sin manejar"
        print request.FILES['file1']
        print request.FILES['file2']
        """
        if lista_vacia(opc1) and lista_vacia(opc2):
            participante_1 = existe_entidad(opc1)
            participante_2 = existe_entidad(opc2)

            if participante_1 and participante_2:
                fusion = fusion_imagen(img1,img2)
                #print fusion.getvalue()
                p1 = formar_participante(opc1,participante_1,'1')
                p2 = formar_participante(opc2,participante_2,'2')
                #p1[0].update(p2[0])
                total = [p1[0],p2[0]]
                #total.update(formar_participante(opc2,participante_2,'2'))

                try:
                    Question.objects.create(for_result_vote=[0,0],usuario_creador=str(request.user.id),asking=pregunta,participante=total,versus=fusion,for_search_cip='%s%s' %(p1[1],p2[1])).save()
                    return HttpResponse("1")
                except Exception, e:
                    print e
                    raise
                    return HttpResponse("0")

            else:
                return HttpResponse("0")
        else:
            return HttpResponse("0")
        #print q
        return HttpResponse("0")
    else:
        return HttpResponse("0")
    # return HttpResponse("Look After You  oh uh oh")

"""
Mensajes para post_versus

1: Se creo el Voto correctamente
0 :error de servidor
"""

def lista_vacia(args):
    for numero in args:
        if numero.strip() == "":
            return False
    return True

def get_or_none(model, **diccionario):
    try:
        if str(diccionario.get('id')).isdigit():
            return model.objects.get(**diccionario)
        else:
            return []
    except model.DoesNotExist:
        return []
    except Exception, e:
        print e
        return None
