from django.urls import path
from .views import CidadeCreate, IndexView, SobreView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('sobre', SobreView.as_view(), name="sobre"),
    path('cadastro', CidadeCreate.as_view(), name="cidade-create" )
]

