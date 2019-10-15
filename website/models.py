from django.db import models
from django import forms    

# Create your models here.

# Criando classe que irá receber todos os emails e senhas cadastrados
class Pessoa(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('NB', 'Não-Binário')
    )
    email = models.EmailField(
        max_length = 255,
        verbose_name = 'Email',
        unique = True
        )
    password = models.CharField(
        max_length = 16,
        verbose_name = 'Senha'
        )
    nome = models.CharField(
        max_length = 32,
        verbose_name = 'Nome'
    )
    data_nascimento = models.DateField(
        null = True
    )
    cep = models.TextField(max_length = 9)
    genero = models.CharField(
        max_length= 13,
        verbose_name='gender',
        choices=GENEROS
    )

    def __str__(self):
        return self.nome

class Item_perdido(models.Model):
    data = models.DateField(
        null = True
        )
    descricao = models.TextField()
    local = models.TextField()
    pessoa = models.ForeignKey(
        "Pessoa",
        on_delete = models.CASCADE
        )
    tags = models.TextField()
    
    def __str__(self):
        return self.local

class Item_achado(models.Model):
    data = models.DateField(
        null = True
        )
    descricao = models.TextField()
    local = models.TextField()
    pessoa = models.ForeignKey(
        "Pessoa",
        on_delete = models.CASCADE
        )
    tags = models.TextField()
    
    def __str__(self):
        return self.local