from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from .models import Cidade, Pessoa

# from DjangoMQTT.cadastros.models import Cidade, Pessoa

# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/modelo.html"

class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"


class CidadeListView(ListView):
    model = Cidade
    template_name = 'listas/cidade.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Cidades'
        context['model'] = 'Cidade'
        context['create_url'] = 'cidade-create'
        context['update_url'] = 'cidade-update'
        context['delete_url'] = 'cidade-delete'
        return context
    
class CidadeCreate(CreateView):
    template_name = "cadastros/formularios.html"
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Cidade'
        return context
    
class CidadeUpdateView(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('cidade-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cidade'
        return context

class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name = 'cadastros/base_confirm_delete.html'
    success_url = reverse_lazy('cidade-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Cidade'
        return context
    

# Pessoa List


class PessoaListView(ListView):
    model = Pessoa
    template_name = 'listas/pessoa.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Pessoas'
        context['create_url'] = 'pessoa-create'
        context['update_url'] = 'pessoa-update'
        context['delete_url'] = 'pessoa-delete'
        return context
    
class PessoaCreateView(CreateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Pessoa'
        return context

class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Pessoa'
        return context

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'cadastros/base_confirm_delete.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Pessoa'
        return context
    
    