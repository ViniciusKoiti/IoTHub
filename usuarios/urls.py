from django.urls import path
from django.contrib.auth import views


urlpatterns = [
  
    path("entrar/", views.LoginView.as_view(
         template_name="cadastros/formularios.html"
         extra_context={
             'titulo' : 'Autenticação de Usuarios'
         })
         , name="login" ),




]



