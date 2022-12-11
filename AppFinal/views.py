from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def registro(request):
    return render(request, "registro.html")

def login(request):
    return render(request, "login.html")

def chat(request):
    return render(request, "chat.html")

