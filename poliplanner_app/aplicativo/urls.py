from django.urls import path
from . import views

app_name = 'aplicativo'
urlpatterns = [
    path('disciplinas/add/', views.create_disciplina, name='add_disciplina'),
    path('disciplinas/', views.DisciplinaListView.as_view(), name='disciplinas'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    path('perfil/<int:pk>/', views.UsuarioDetailView.as_view(), name='detail_perfil'),
    path('perfil/delete/<int:pk>/', views.UsuarioDeleteView.as_view(), name='delete_perfil'),
    path('aula/create/', views.create_aula, name='create_aula'),
]