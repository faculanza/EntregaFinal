from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormNuevoBlog(forms.Form):
    titulo = forms.CharField(min_length=3)
    subtitulo = forms.CharField()
    resumen = forms.CharField(widget=forms.Textarea)
    cuerpo = forms.CharField(widget=forms.Textarea)
    #resumen = forms.Textarea()
    #cuerpo= forms.TextInput()
    
class FormComentario(forms.Form):
    comentario = forms.CharField(min_length=3, widget=forms.Textarea)

class FormMensaje(forms.Form):
    destinatario = forms.ModelChoiceField(label="Destinatario",queryset=User.objects.all())
    mensaje = forms.CharField(widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]
