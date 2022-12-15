from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFinal.models import Blogs
from AppFinal.forms import FormNuevoBlog, UserRegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    blogs = Blogs.objects.all() # Obtener TODOS los registros de ese modelo
    # Creamos el contexto
    contexto = {"listado_blogs": blogs}
    
    return render(request, "index.html", contexto)


def about(request):
    return render(request, "about.html")

def NuevoBlog(request):
    if request.method == "POST":
        miFormulario = NuevoBlog(request.POST)
        
        if miFormulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = miFormulario.cleaned_data

            nBlog = Blogs(titulo=data["titulo"], subtitulo=data["subtitulo"], resumen=data["resumen"], contenido=data["contenido"], email=data["amail"])
            nBlog.save()
            return render(request, "index.html")
            
    miFormulario = FormNuevoBlog()
    return render(request, "nuevo_blog.html", {"miFormulario": miFormulario})

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            return render(request, "index.html")
        else:
            return render(request, "registro.html", { "form": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "registro.html", { "form": formulario})


def loginPage(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "login.html", {"form": formulario, "errors": errors})

def chat(request):
    return render(request, "chat.html")



