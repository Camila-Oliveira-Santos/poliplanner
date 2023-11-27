from django.db import models
from django import forms
from django.conf import settings
from usuarios.models import Usuario

class Disciplina(models.Model):
    titulo = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.titulo}'

class Dia(models.Model):
    dia = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.dia}'

class Horario(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=0)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE, default=0)
    inicio = models.CharField(max_length=20, default=0)
    fim = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f'{self.dia} ({self.inicio} - {self.fim})'

class Aula(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, default=0)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=0)
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0, related_name='professor_aula')
    alunos = models.ManyToManyField(Usuario, related_name='alunos_aula')

    def __str__(self):
        return f'{self.professor} - {self.disciplina}'

class Feedback(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    texto = models.TextField(default=None)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'"{self.texto}" - {self.autor.username}'