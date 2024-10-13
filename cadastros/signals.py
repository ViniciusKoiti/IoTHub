
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario, Pessoa

@receiver(post_save, sender=User)
def criar_usuario(sender, instance, created, **kwargs):
    if created:
        pessoa = Pessoa.objects.create(
            primeiro_nome=instance.username,  
            sobrenome='',
            cpf='000.000.000-00',  
            email=instance.email
        )
        Usuario.objects.create(user=instance, pessoa=pessoa)
    else:
        try:
            instance.usuario.save()
        except Usuario.DoesNotExist:
            pessoa = Pessoa.objects.create(
                primeiro_nome=instance.username,
                sobrenome='',
                cpf='000.000.000-00',
                email=instance.email
            )
            Usuario.objects.create(user=instance, pessoa=pessoa)
