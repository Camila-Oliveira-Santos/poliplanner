from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Disciplina, Horario, Aula, Feedback
from usuarios.models import Usuario
from .forms import DisciplinaForm, FeedbackForm, HorarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def create_disciplina(request):
    if request.method == 'POST':
        disciplina_form = DisciplinaForm(request.POST)
        if disciplina_form.is_valid():
            disciplina = Disciplina(**disciplina_form.cleaned_data)
            disciplina.save()
            return HttpResponseRedirect(
                reverse('aplicativo:disciplinas'))
    else:
        disciplina_form = DisciplinaForm()
    context = {'disciplina_form': disciplina_form}
    return render(request, 'aplicativo/add_disciplina.html', context)

class DisciplinaListView(generic.ListView):
    model = Disciplina
    template_name = 'aplicativo/lista_disciplinas.html'

class UsuarioDetailView(generic.DetailView):
    model = Usuario
    template_name = "aplicativo/detail_perfil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UsuarioListView(generic.ListView):
    model = Usuario
    template_name = "aplicativo/lista_usuarios.html"

class UsuarioDeleteView(generic.DeleteView):
    model = Usuario
    template_name = "aplicativo/delete_usuario.html"
    success_url = reverse_lazy('aplicativo:usuarios')

class AulaCreateView(generic.CreateView):
    model = Aula
    template_name = "aplicativo/create_aula.html"
    fields = ['disciplina']
    horario_form = HorarioForm()

def create_aula(request):
    if request.method == 'POST':
        horario_form = HorarioForm(request.POST)
        if horario_form.is_valid():
            horario = Horario(**horario_form.cleaned_data)
            horario.save()
            return HttpResponseRedirect(
                reverse('index'))
    else:
        horario_form = HorarioForm()
    context = {'horario_form': horario_form}
    return render(request, 'aplicativo/create_aula.html', context)

class FeedbackCreateView(generic.CreateView):
    model = Feedback
    template_name = "aplicativo/feedback.html"