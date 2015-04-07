from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class FormRegistrarUsuario(forms.Form):
	registro_input_nombre_completo = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'class':'form-control','id':'r_input_name_complete','placeholder':'Nombre Completo'}))
	registro_input_email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','id':'r_input_email','placeholder':'Correo Electronico'}))
	registro_input_password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','id':'r_input_password','placeholder':'Contrasena'})) #,render_value=True
	registro_input_usuario = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','id':'r_input_usuario','placeholder':'Nombre de Usuario'}))	

class FormInciarSesion(forms.Form):
	username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','id':'s_input_email','placeholder':'Correo Electronico'}))
	password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','id':'s_input_password','placeholder':'Contrasena'}))
#iniciar_input_email
#iniciar_input_password