from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Clientes, Servicos

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
    
    return render(request,'cadastro1.html')

def cadastro2(request):
    if request.method == 'POST':
       descricao = request.POST.get('descricao')
       preco = request.POST.get('preco')
       data = request.POST.get('data')
    
    return render(request,'cadastro2.html')

def consulta1(request):
    return render(request,'consulta1.html')

def consulta2(request):
    return render(request,'consulta2.html')

def excluir1(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    #select * from Clientes_clientes where id = 1
    cliente.delete()
    
    return render(request,)

def editar1(request, id):
    cliente = get_object_or_404(Clientes, id=id)
     
    if request.method == 'POST':
        cliente.username = request.POST.get('username')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')

        cliente.save()
    
    return render(request,'editar1.html')
