from django.apps import AppConfig


class CadastrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastros'

    def ready(self):
        import cadastros.signals  # Importa os signals para que sejam registrados