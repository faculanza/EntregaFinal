from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFinal.models import Blogs, Comentarios, Mensajes
from AppFinal.forms import FormNuevoBlog, UserRegisterForm, FormComentario, FormMensaje
from datetime import date, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def inicio(request):
    blogs = Blogs.objects.all() # Obtener TODOS los registros de ese modelo
    # Creamos el contexto
    contexto = {"listado_blogs": blogs}
    return render(request, "index.html", contexto)    

def about(request):
    return render(request, "about.html")

# --------------------------------------------------------
# ----------- R E G I S T R O  /  L O G I N --------------
# --------------------------------------------------------

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
                
                blogs = Blogs.objects.all()
                contexto = {"listado_blogs": blogs}
                return render(request, "index.html", contexto) 

            else:
                return render(request, "login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "login.html", {"form": formulario})


# --------------------------------------------------------
# ----------- B L O G S --------------
# --------------------------------------------------------
def NuevoBlog(request):
    if request.method == "POST":
        miFormulario = FormNuevoBlog(request.POST)
        
        if miFormulario.is_valid():
            # Accedemos al diccionario que contiene
            # la informacion del formulario
            data = miFormulario.cleaned_data

            nBlog = Blogs(titulo=data["titulo"], subtitulo=data["subtitulo"], resumen=data["resumen"], cuerpo=data["cuerpo"], idusuario=request.user.id, fecha=date.today(),usuario=request.user.username)
            nBlog.save()
        
            blogs = Blogs.objects.all() # Obtener TODOS los registros de ese modelo
            contexto = {"listado_blogs": blogs}
            return render(request, "index.html", contexto)
        else:
            errores = formulario.errors
            miFormulario = FormNuevoBlog()
            return render(request, "nuevo_blog.html", {"miFormulario": miFormulario})
    else:
        miFormulario = FormNuevoBlog()
        return render(request, "nuevo_blog.html", {"miFormulario": miFormulario})

def blogAmpliado(request, id):
    if request.method == "POST":
        formulario = FormComentario(request.POST)
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
                       
            agrComent = Comentarios(comentario=data["comentario"],idblog=id,idusuario=request.user.id, fecha=date.today(),usuario=request.user.username)
            agrComent.save()

    blogs = Blogs.objects.get(id=id)
    coments = Comentarios.objects.filter(idblog=id)
    formulario = FormComentario()
    contexto = {"listado_blogs": blogs, "form": formulario, "listado_coments": coments}
    
    return render(request, "blogAmpliado.html", contexto)  

def editarBlog(request, id):
    blog = Blogs.objects.get(id=id)
    
    if request.method == "POST":
        formulario = FormNuevoBlog(request.POST)
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            blog.titulo = data["titulo"]
            blog.subtitulo = data["subtitulo"]
            blog.resumen = data["resumen"]
            blog.cuerpo = data["cuerpo"]
            blog.echa=date.today()
            blog.save()
 
            blogs = Blogs.objects.get(id=id)
            coments = Comentarios.objects.filter(idblog=id)
            formulario = FormComentario()
            contexto = {"listado_blogs": blogs, "form": formulario, "listado_coments": coments}
            
            return render(request, "blogAmpliado.html", contexto)
    
    else:
        formulario = FormNuevoBlog(initial={"titulo": blog.titulo, "subtitulo": blog.subtitulo, "resumen": blog.resumen, "cuerpo":blog.cuerpo})
        return render(request, "editar_blog.html", {"formulario": formulario})

def eliminarComent(request, id, idblog):
    coment = Comentarios.objects.get(id=id)
    coment.delete()

    blogs = Blogs.objects.get(id=idblog)
    coments = Comentarios.objects.filter(idblog=idblog)
    formulario = FormComentario()
    contexto = {"listado_blogs": blogs, "form": formulario, "listado_coments": coments}
    
    return render(request, "blogAmpliado.html", contexto)  

def eliminarBlog(request, id):
    coment = Blogs.objects.get(id=id)
    coment.delete()

    #coment = Comentarios.objects.get(idblog=id)
    coment = Comentarios.objects.filter(idblog=id)
    coment.delete()

    blogs = Blogs.objects.all()
    contexto = {"listado_blogs": blogs}
    return render(request, "index.html", contexto)


# --------------------------------------------------------
# ----------- C H A T S --------------
# --------------------------------------------------------

def chat(request):
    if request.method == "POST":
        formulario = FormMensaje(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            agrMen = Mensajes(mensaje=data["mensaje"],hora=datetime.now(),idautor=request.user.id, fecha=date.today(),destinatario=data["destinatario"],autor=request.user.username)
            agrMen.save()

    formulario = FormMensaje()
    users = User.objects.all()
    misMsg = Mensajes.objects.filter(idautor=request.user.id)
    MsgAmi = Mensajes.objects.filter(destinatario=request.user.username)
    contexto = {"listado_users": users, "formulario":formulario, "misMensajes":misMsg, "MensAmi":MsgAmi}

    return render(request, "chat.html", contexto)

def eliminarMensaje(request, id):
    coment = Mensajes.objects.get(id=id)
    coment.delete()
    
    formulario = FormMensaje()
    users = User.objects.all()
    misMsg = Mensajes.objects.filter(idautor=request.user.id)
    MsgAmi = Mensajes.objects.filter(destinatario=request.user.username)
    contexto = {"listado_users": users, "formulario":formulario, "misMensajes":misMsg, "MensAmi":MsgAmi}
    return render(request, "chat.html", contexto)



