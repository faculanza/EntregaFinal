from django.urls import path
from AppFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('',views.inicio, name='inicio'),
    path('about/',views.about, name='about'),  
    path('registro/',views.registro, name='registro'),  
    path('loginPage/',views.loginPage, name='loginPage'),  
    path('chat/',views.chat, name='chat'),
    # path('AgregarCategoria/',views.AgregarCategoria, name='AgregarCategoria'),
    # path('AgregarProducto/',views.AgregarProducto, name='AgregarProducto'),
    # path('buscarproducto/',views.buscarproducto, name='buscarproducto'),
    # path('resultado_producto/',views.resultado_producto, name='resultado_producto'),

    


]