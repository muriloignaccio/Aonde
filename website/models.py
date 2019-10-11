from django.db import models
from django import forms    

# Create your models here.

# Criando classe que irá receber todos os emails e senhas cadastrados
class User(models.Model):
    email = models.EmailField(max_length = 255, verbose_name = 'Email', unique = True)
    password = models.CharField(max_length = 16, verbose_name = 'Senha')

    def __str__(self):
        return self.email

class Cadastro(models.Model):
    nome = models.CharField(max_length = 32, verbose_name = 'Nome')
    data_nascimento = models.DateField()

# class UserForm(forms.Form):
#     birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)