from django.urls import path
from .views import CidadeCreate,CidadeUpdateView, RelesCreateView, RelesDeleteView, RelesListView, RelesUpdateView
from .views import IndexView, SobreView, CidadeListView, CidadeDeleteView ,PessoaListView 
from .views import PessoaCreateView, PessoaUpdateView, PessoaDeleteView, SensorListView
from .views import SensorCreateView, SensorDeleteView, SensorUpdateView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('sobre', SobreView.as_view(), name="sobre"),

    # Cidades
    path('cidades/',CidadeListView.as_view(), name='cidade-list'),
    path('cidades/form', CidadeCreate.as_view(), name="cidade-create" ),
    path('cidades/update/<int:pk>/', CidadeUpdateView.as_view(), name='cidade-update'),
    path('cidades/delete/<int:pk>/', CidadeDeleteView.as_view(), name='cidade-delete'),

    # Pessoa

    path('pessoas/', PessoaListView.as_view(), name='pessoa-list'),
    path('pessoas/create/', PessoaCreateView.as_view(), name='pessoa-create'),
    path('pessoas/update/<int:pk>/', PessoaUpdateView.as_view(), name='pessoa-update'),
    path('pessoas/delete/<int:pk>/', PessoaDeleteView.as_view(), name='pessoa-delete'),

    # Sensores

    path('sensores/', SensorListView.as_view(), name='sensor-list'),
    path('sensores/create/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensores/update/<int:pk>/', SensorUpdateView.as_view(), name='editar-sensor'),
    path('sensores/delete/<int:pk>/', SensorDeleteView.as_view(), name='excluir-sensor'),

    path('sensores/', RelesListView.as_view(), name='reles-list'),
    path('sensores/create/', RelesCreateView.as_view(), name='reles-create'),
    path('sensores/update/<int:pk>/', RelesUpdateView.as_view(), name='reles-sensor'),
    path('sensores/delete/<int:pk>/', RelesDeleteView.as_view(), name='reles-sensor'),


]

