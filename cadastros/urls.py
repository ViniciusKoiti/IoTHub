from django.urls import path
from .views import CidadeCreate, CidadeUpdateView ,IndexView, SobreView, CidadeListView, CidadeDeleteView ,PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView


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
]

