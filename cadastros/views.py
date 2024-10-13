from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.db.models import Count

from .models import (
    Dispositivos, Sensor, Leitura, Microcontrolador, 
    Acessos, Usuario,Cidade,Pessoa, Reles
)

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "cadastros/modelo.html"  # Atualize para o template correto
    login_url = 'login'  # URL para redirecionar se não estiver logado
    redirect_field_name = 'redirect_to'  # Nome do campo de redirecionamento (opcional)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            print(self.request.user)
        
            usuario = self.request.user.usuario.pessoa
            context['usuario'] = usuario
        except Usuario.DoesNotExist:
            context['usuario'] = None  # ou algum valor padrão

        context['ultimos_dispositivos'] = Dispositivos.objects.order_by('-data_criacao')[:5]

        context['ultimas_leituras'] = Leitura.objects.select_related('sensor').order_by('-data_criacao')[:10]

        context['resumo_sensores'] = Sensor.objects.values('tipo').annotate(total=Count('id'))

        context['microcontroladores_acessos'] = Microcontrolador.objects.select_related('conexao').prefetch_related('acessos_set')[:5]

        context['ultimos_acessos'] = Acessos.objects.select_related('usuario__pessoa', 'microcontrolador').order_by('-data_criacao')[:5]

        context['ultima_atualizacao'] = timezone.now()

        return context


class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"


class CidadeListView(LoginRequiredMixin,ListView):
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
    
class CidadeCreate(LoginRequiredMixin,CreateView):
    template_name = "cadastros/formularios.html"
    model = Cidade
    success_url = reverse_lazy('cidade-list')
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Cidade'
        return context
    
class CidadeUpdateView(LoginRequiredMixin,UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('cidade-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cidade'
        return context

class CidadeDeleteView(GroupRequiredMixin,DeleteView):
    model = Cidade
    template_name = 'cadastros/base_confirm_delete.html'
    success_url = reverse_lazy('cidade-list')
    group_required = ["Administrador"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Cidade'
        return context
    

# Pessoa List


class PessoaListView(LoginRequiredMixin,ListView):
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
    
class PessoaCreateView(LoginRequiredMixin,CreateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Pessoa'
        context['model'] = 'Pessoa'
        return context

class PessoaUpdateView(LoginRequiredMixin,UpdateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Pessoa'
        return context

class PessoaDeleteView(LoginRequiredMixin,DeleteView):
    model = Pessoa
    template_name = 'cadastros/base_confirm_delete.html'
    success_url = reverse_lazy('pessoa-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Pessoa'
        return context
    
 #Sensores Listas View   
    
class RelesListView(LoginRequiredMixin,ListView):
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

class RelesCreateView(LoginRequiredMixin,CreateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('reles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Reles'
        return context

class RelesUpdateView(LoginRequiredMixin,UpdateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('reles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Reles'
        return context

class RelesDeleteView(GroupRequiredMixin,DeleteView):
    model = Reles
    template_name = 'cadastro/base_confirm_delete.html'
    success_url = reverse_lazy('reles-list')
    group_required = ["Administrador"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Reles'
        return context    
    
# Reles testes

class SensorListView(LoginRequiredMixin,ListView):
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

class SensorCreateView(LoginRequiredMixin,CreateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Sensor'
        return context

class SensorUpdateView(LoginRequiredMixin,UpdateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Sensor'
        return context

class SensorDeleteView(GroupRequiredMixin,DeleteView):
    model = Sensor
    template_name = 'cadastro/base_confirm_delete.html'
    success_url = reverse_lazy('sensor-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar Sensor'
        return context    