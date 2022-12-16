from django.urls import path
from AppFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('',views.inicio, name='inicio'),
    path('about/',views.about, name='about'),  
    path('registro/',views.registro, name='registro'),  
    path('loginPage/',views.loginPage, name='loginPage'), 
    path('chat/',views.chat, name='chat'),
    path('NuevoBlog/',views.NuevoBlog, name='NuevoBlog'),
    path('blogAmpliado/<id>/',views.blogAmpliado, name='blogAmpliado'),
    path("logoutPage/", LogoutView.as_view(template_name='logout.html'), name="logoutPage"),
      


]