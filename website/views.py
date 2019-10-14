from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        formulario_email = request.POST['email']
        formulario_senha = request.POST['senha']
        print(formulario_email)
        print(formulario_senha)

        usuario_logado = Pessoa.objects.filter(email = formulario_email, 
                                               password = formulario_senha).first()
        
        if usuario_logado is not None:
            args = {
                'msg': usuario_logado
            }
            return render(request, 'index.html', args)
        args = {
            'msg': 'Fazer login novamente!'
        }
        print('passou pelo args do else')
        return render(request, 'index.html', args)
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        data = Pessoa()
        data.nome = request.POST['nome']
        data.email = request.POST['email']
        data.password = request.POST['senha']
        data.data_nascimento = request.POST['nascimento']
        data.cep = request.POST['cep']
        data.genero = request.POST['gender']
        data.save()

        args = {
            'aviso': 'Cadastrado'
        }
        return render(request, 'cadastro.html', args)

    return render(request, 'cadastro.html')

def aonde(request):
    return render(request, 'aonde.html')

def perdi (request):
    if request.method == 'POST':
        dados = Item_perdido()
        dados.descricao = request.POST['descricaoPerdeu']
        dados.local = request.POST['localPerdeu']
        dados.data = request.POST['dataPerdeu']
        dados.tags = request.POST['tagsPerdeu']
        dados.save()

        return render (request, 'perdi.html')
    return render(request, 'perdi.html')