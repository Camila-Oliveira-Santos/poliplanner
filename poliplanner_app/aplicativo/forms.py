from django.forms import ModelForm
from .models import Disciplina, Horario, Aula, Feedback, Dia


class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = [
            'titulo',
            'codigo',
        ]
        labels = {
            'titulo': 'Nome da Disciplina',
            'codigo': 'Código da Disciplina',
        }

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'texto',
        ]
        labels = {
            'texto': 'Comentários',
        }

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = [
            'dia',
            'inicio',
            'fim',
        ]
        labels = {
            'dia': 'Dias da Semana',
            'inicio': 'De:',
            'fim':'Até:',
        }