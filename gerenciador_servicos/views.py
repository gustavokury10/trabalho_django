from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Clientes, Servicos


@login_required
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')


@login_required
def cadastrocliente(request):
    if request.method == 'POST':
        Clientes.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            cpf=request.POST.get('cpf'),
        )
        return redirect('consultacliente')
    return render(request, 'cadastrocliente.html')


@login_required
def consultacliente(request):
    clientes = Clientes.objects.all()
    return render(request, 'consultacliente.html', {'clientes': clientes})


@login_required
@require_POST
def excluir1(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    cliente.delete()
    return redirect('consultacliente')


@login_required
def editar1(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')
        cliente.save()
        return redirect('consultacliente')
    return render(request, 'editar1.html', {'cliente': cliente})


@login_required
def cadastro2(request):
    if request.method == 'POST':
        Servicos.objects.create(
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            ativo=request.POST.get('ativo') == 'on',
        )
        return redirect('consulta2')
    return render(request, 'cadastro2.html')

@login_required
def editar2(request, id):
    servico = get_object_or_404(Servicos, id=id)
    if request.method == 'POST':
        servico.descricao = request.POST.get('descricao')
        servico.preco = request.POST.get('preco')
        servico.ativo = request.POST.get('ativo') == 'on'
        servico.save()
        return redirect('consulta2')
    return render(request, 'edicao2.html', {'servico': servico})

@login_required
def consulta2(request):
    servicos = Servicos.objects.all()
    return render(request, 'consulta2.html', {'servicos': servicos})

@login_required
@require_POST
def excluir2(request, id):
    servico = get_object_or_404(Servicos, id=id)
    servico.delete()
    return redirect('consulta2')