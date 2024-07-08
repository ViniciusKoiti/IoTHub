from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "cadastros/modelo.html"

class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"