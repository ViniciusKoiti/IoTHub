from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .models import Cidade

# from DjangoMQTT.cadastros.models import Cidade, Pessoa

# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/modelo.html"

class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"

class CidadeCreate(CreateView):
    template_name = "cadastros/formularios.html"
    model = Cidade
    fields = ['nome', 'estado']
    
    

