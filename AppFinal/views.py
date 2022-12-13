from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFinal.models import Usuarios
from AppFinal.forms import AgreReg

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def registro(request):
    if request.method == "POST":
        miFormulario = AgreReg(request.POST)
        
        if miFormulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = miFormulario.cleaned_data

            registracion = Usuarios(nombre=data["nombre"], apellido=data["apellido"], usuario=data["usuario"], password=data["password"], email=data["email"])
            registracion.save()
            return render(request, "inicio.html")
            
    miFormulario = AgreReg()
    return render(request, "registro.html", {"miFormulario": miFormulario})

# def registro(request):
#     if request.method == "POST":
#         formulario = UserRegisterForm(request.POST)

#         if formulario.is_valid():
            
#             formulario.save()
#             return redirect("inicio")
#         else:
#             return render(request, "registro.html", { "form": formulario, "errors": formulario.errors})

#     formulario  = UserRegisterForm()
#     return render(request, "registro.html", { "form": formulario})


def login(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["usuario"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "login.html", {"form": formulario, "errors": errors})

def chat(request):
    return render(request, "chat.html")

