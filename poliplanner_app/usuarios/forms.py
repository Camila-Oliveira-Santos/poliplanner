from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'email',
            'is_aluno',
            'is_professor',
        ]
        labels = {
            'nome': 'Nome Completo',
            'email': 'Email Institucional',
            'is_aluno':'Aluno?',
            'is_professor':'Professor?',
        }