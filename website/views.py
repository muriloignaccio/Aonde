from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        try:
            usuario = Pessoa.objects.get(email = request.POST['email'])
        except Pessoa.DoesNotExist:
            usuario = None
        if usuario is not None:
            request.session['nome'] = usuario.nome
            if usuario.password == request.POST['senha']:
                return redirect("/aonde")
            else:
                args = {
                    'msg': 'Senha Incorreta'
                }
                return render(request, 'login.html', args)
        else:
            print('ci')
            args = {
                'msg': 'Usuário não encontrado'
            }
            return render(request, 'login.html', args)
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        dados_cadastro = Pessoa()
        dados_cadastro.nome = request.POST['nome']
        dados_cadastro.email = request.POST['email']
        dados_cadastro.password = request.POST['senha']
        dados_cadastro.data_nascimento = request.POST['nascimento']
        dados_cadastro.cep = request.POST['cep']
        dados_cadastro.genero = request.POST['gender']
        dados_cadastro.save()

        args = {
            'aviso': 'Cadastrado'
        }
        return render(request, 'cadastro.html', args)

    return render(request, 'cadastro.html')

def aonde(request):
    return render(request, 'aonde.html')

def perdi (request):
    nome_usuario = Pessoa.objects.get(nome = request.session['nome'])
    if request.method == 'POST':
        item_perdido = Item_perdido()
        item_perdido.pessoa = nome_usuario
        item_perdido.descricao = request.POST['descricaoPerdeu']
        item_perdido.imagem = request.POST['imagemPerdida']
        item_perdido.local = request.POST['localPerdeu']
        item_perdido.data = request.POST['dataPerdeu']
        item_perdido.tags = request.POST['tagsPerdeu']
        item_perdido.save()

        return render (request, 'perdi.html')
    return render(request, 'perdi.html')

def achei (request):
    nome_usuario = Pessoa.objects.get(nome = request.session['nome'])
    if request.method == 'POST':
        item_achado = Item_achado()
        item_achado.pessoa = nome_usuario
        item_achado.descricao = request.POST['descricaoAchou']
        item_achado.imagem = request.POST['imagemAchado']
        item_achado.local = request.POST['localAchou']
        item_achado.data = request.POST['dataAchou']
        item_achado.tags = request.POST['tagsAchou']
        item_achado.save()

        return render (request, 'achei.html')
    return render(request, 'achei.html')