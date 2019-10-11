from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        data = Pessoa()
        data.nome = request.
    return render(request, 'cadastro.html')