# -*- encoding: utf-8 -*-
#Script creado por mi para los formularios capt. 8 y 9 del tutorial
from django import forms
from django.contrib.auth.models import User
from bares.models import Tapas

class TapasForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Por favor introduzca el nombre de la tapa.")

    class Meta:
        # Asociacion entre el ModelForm y el model
        model = Tapas
        # ¿Que campos queremos introducir en el formulario?
        # No necesitamos todos los campos del modelo actual
        # Los campos que permiten NULL podemos no incluirlos
        # Ocultamos la clave externa
        # la excluimos de la siguiente forma
        exclude = ('n_bar',)
        #o podemos especificar los campos a incluir
        #fields = ('nombre', 'votos')

class RegisterForm(forms.ModelForm):
	username = forms.SlugField(max_length=10, label='Usuario')
	email = forms.EmailField(label='Email')
	password = forms.SlugField(max_length=10,widget=forms.PasswordInput(),label='Contraseña')

	class Meta: 
		model = User
		fields = ('username', 'email', 'password')

class login_form(forms.ModelForm): 
	username = forms.SlugField(max_length=10, label='Usuario')
	password = forms.SlugField(max_length=10, widget=forms.PasswordInput(), label='Contraseña')

	class Meta: 
		model = User
		fields = ('username', 'password')