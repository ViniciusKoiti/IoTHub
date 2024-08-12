from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from .models import Cidade, Pessoa, Reles, Sensor

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
    success_url = reverse_lazy('cidade-list')
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
        context['model'] = 'Pessoas'
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
        context['model'] = 'Pessoa'
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
    
 #Sensores Listas View   
    
class RelesListView(ListView):
    model = Reles
    template_name = 'listas/reles.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Reles'
        context['model'] = 'Reles'
        context['create_url'] = 'reles-create'
        context['update_url'] = 'reles-update'
        context['delete_url'] = 'reles-delete'
        return context

class RelesCreateView(CreateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('reles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Reles'
        return context

class RelesUpdateView(UpdateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('reles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Reles'
        return context

class RelesDeleteView(DeleteView):
    model = Reles
    template_name = 'cadastro/base_confirm_delete.html'
    success_url = reverse_lazy('reles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Reles'
        return context    
    
# Reles testes

class SensorListView(ListView):
    model = Sensor
    template_name = 'listas/sensor.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Sensores'
        context['model'] = 'Sensor'
        context['create_url'] = 'sensor-create'
        context['update_url'] = 'sensor-update'
        context['delete_url'] = 'sensor-delete'
        return context

class SensorCreateView(CreateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Sensor'
        return context

class SensorUpdateView(UpdateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Sensor'
        return context

class SensorDeleteView(DeleteView):
    model = Sensor
    template_name = 'cadastro/base_confirm_delete.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Sensor'
        return context    