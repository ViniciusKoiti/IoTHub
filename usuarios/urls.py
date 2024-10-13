from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(
        template_name='cadastros/formularios.html',
        extra_context={
            'titulo': 'Autenticação de Usuarios',
            'botao_sucesso': 'Login',
        }), name='login'),

    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('senha/', auth_views.PasswordChangeView.as_view(), name="alterar-senha"),
    path('minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name="cadastro/formulario.html",
        success_url= reverse_lazy("index"),
        extra_context={
            'titulo': 'Atualizar minha senha'
        }
    ), name="alterar-senha"),
    path('registrar/', views.RegistroView.as_view(), name='registrar'),
]
