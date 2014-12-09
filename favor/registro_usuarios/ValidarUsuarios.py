from django.contrib.auth.models import User
class ValidarUsuario():

    def validarEmail(self,dato):
        rpta={}
        print dato
        if '@' in dato:
            us=User.objects.filter(email__iexact=dato)
            #1-> Si existe - 0->No existe
            rpta['valido'] = "1" if us else "0"
            #print valor
            
            #Consultar
        else:
            #3->Email Invalido - 4->Cadena Vacio
            rpta['valido'] = "3" if len(dato)!=0 else "4"
        return rpta
           # if dato.length==0:
            #    print "No hay data"
           # print "Este email no es valido"

    def validarNombre(self,dato):
        rpta={}
        #0->Si  dato, tiene elementos
        #4->Si dato, es vacia 
        rpta['valido'] = "0" if len(dato)!=0 else "4"
        return rpta

    def validarPassword(self,dato):
        rpta={}
        #0->Si  dato,tiene 6 o mas caracteres.
        #4->Si dato, tiene 5 o menos caracteres. 
        rpta['valido'] = "0" if len(dato)>=6 else "4"
        return rpta

    def validarUsername(self,dato):
        rpta={}
        if len(dato) < 1:
            #4-> Si dato, es vacio
            rpta['valido'] = "4"
        else:
            us=User.objects.filter(username__iexact=dato)
            print us
            #1->Si existe ese username
            #0->No existe, es libre.
            rpta['valido'] = "1" if us else "0"

        return rpta

    def validarTodos(self,nombre='',email='',password='',username=''):
        return {'validoN': self.validarNombre(nombre).get('valido',''),
        'validoE': self.validarEmail(email).get('valido',''),
        'validoP': self.validarPassword(password).get('valido',''),
        'validoU': self.validarUsername(username).get('valido','')}
        #,self.validarEmail(email),self.validarPassword(password),self.validarUsername(username)}

    def passwordZero(self,password=''):
        if len(password)> 5:
            return True
        return False

    def passwordFirst(self, password=''):
        if len(password)> 5:
            return True
        return False

    def passwordSecond(self, password1, password2):
        if len(password2) <6 :
            return False
        elif password1 == password2:
            return True
        else:
            return False
