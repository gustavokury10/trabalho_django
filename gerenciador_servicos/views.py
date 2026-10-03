from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
       return render(request, 'home.html')
    else:
        return render(request, 'login.html')

def cadastro1(request):
    if request.method == 'POST':
       nome = request.POST.get('nome')
       email = request.POST.get('email')
       telefone = request.POST.get('telefone')
       cpf = request.POST.get('cpf')
    
    return render(request,'cadastro.html')

