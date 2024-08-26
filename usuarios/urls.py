from django.urls import path, reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    path('entrar/', views.LoginView.as_view(
        template_name='cadastros/formularios.html',
        extra_context={
            'titulo': 'Autenticação de Usuarios'
        }), name='login'),

    path('sair/', views.LogoutView.as_view(), name='logout'),
    path('senha/', views.PasswordChangeView.as_view(), name="alterar-senha"),
    path('minha-senha/', views.PasswordChangeView.as_view(
        template_name="cadastro/formulario.html",
        success_url= reverse_lazy("index"),
        extra_context={
            'titulo': 'Atualizar minha senha'
        }
    ), name="alterar-senha"),
]
