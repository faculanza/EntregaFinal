from django import forms

class AgreReg(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    usuario = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()

# class UserRegisterForm(UserCreationForm):
#     mombre = forms.CharField()
#     apellido = forms.CharField()
#     usuario = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = Usuarios
#         fields = ['nombre','apellido','email','usuario','password']
#         help_texts = {k:"" for k in fields}
