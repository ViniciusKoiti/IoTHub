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

class BaseListView(LoginRequiredMixin, ListView):
    template_name = 'listas/base_list.html'  # Template padrão (pode ser sobrescrito)
    context_object_name = 'objects'  # Nome padrão do contexto (pode ser sobrescrito)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo  # Título dinâmico vindo da classe específica
        context['model'] = self.model_name  # Nome do modelo vindo da classe específica
        context['create_url'] = self.create_url
        context['update_url'] = self.update_url
        context['delete_url'] = self.delete_url
        return context

class CidadeListView(BaseListView):
    template_name = 'listas/cidade.html'
    model = Cidade
    titulo = 'Lista de Cidades'
    model_name = 'Cidade'
    create_url = 'cidade-create'
    update_url = 'cidade-update'
    delete_url = 'cidade-delete'

class BaseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cadastros/formularios.html'
    success_url = reverse_lazy('home')  # Sobrescreva nas classes específicas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context
    
    def form_valid(self, form):
        usuario_logado = self.request.user.usuario  
        form.instance.criador = usuario_logado
        form.instance.atualizado_por = usuario_logado
        return super().form_valid(form)

class BaseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/formularios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context
    
class BaseDeleteView(GroupRequiredMixin, DeleteView):
    template_name = 'cadastros/base_confirm_delete.html'
    group_required = ["Administrador"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class CidadeCreate(BaseCreateView):
    model = Cidade
    fields = ['nome', 'estado']
    titulo = 'Adicionar Cidade'
    success_url = reverse_lazy('cidade-list')

    
class CidadeUpdateView(BaseUpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    titulo = 'Editar Cidade'
    success_url = reverse_lazy('cidade-list')

class CidadeDeleteView(BaseDeleteView):
    model = Cidade
    titulo = 'Deletar Cidade'
    success_url = reverse_lazy('cidade-list')
    

# Pessoa List

class PessoaListView(BaseListView):
    template_name = 'listas/pessoa.html'
    model = Pessoa
    titulo = 'Lista de Pessoas'
    model_name = 'Pessoa'
    create_url = 'pessoa-create'
    update_url = 'pessoa-update'
    delete_url = 'pessoa-delete'
    
class PessoaCreateView(BaseCreateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    titulo = 'Adicionar Pessoa'
    success_url = reverse_lazy('pessoa-list')
class PessoaUpdateView(BaseUpdateView):
    model = Pessoa
    fields = ['primeiro_nome', 'sobrenome', 'cpf', 'email']
    titulo = 'Editar Pessoa'
    success_url = reverse_lazy('pessoa-list')
    
class PessoaDeleteView(BaseDeleteView):
    model = Pessoa
    titulo = 'Deletar Pessoa'
    success_url = reverse_lazy('pessoa-list')
    
 #Sensores Listas View   
    
class RelesListView(BaseListView):
    template_name = 'listas/reles.html'
    model = Reles
    titulo = 'Lista de Reles'
    model_name = 'Reles'
    create_url = 'reles-create'
    update_url = 'reles-update'
    delete_url = 'reles-delete'

class RelesCreateView(BaseCreateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    titulo = 'Adicionar Reles'
    success_url = reverse_lazy('reles-list')

class RelesUpdateView(BaseUpdateView):
    model = Reles
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    titulo = 'Editar Reles'
    success_url = reverse_lazy('reles-list')

class RelesDeleteView(BaseDeleteView):
    model = Reles
    titulo = 'Deletar Reles'
    success_url = reverse_lazy('reles-list')  
    
# Reles testes
class SensorListView(BaseListView):
    template_name = 'listas/sensor.html'
    model = Sensor
    titulo = 'Lista de Sensores'
    model_name = 'Sensor'
    create_url = 'sensor-create'
    update_url = 'sensor-update'
    delete_url = 'sensor-delete'

class SensorCreateView(BaseCreateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    titulo = 'Adicionar Sensor'
    success_url = reverse_lazy('sensor-list')

class SensorUpdateView(BaseUpdateView):
    model = Sensor
    fields = ['descricao', 'data_instalacao', 'ultima_manutencao', 'tipo']
    titulo = 'Editar Sensor'

class SensorDeleteView(BaseDeleteView):
    model = Sensor
    titulo = 'Deletar Sensor'
    success_url = reverse_lazy('sensor-list')