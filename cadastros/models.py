from django.db import models
from django.contrib.auth.models import User


class Auditoria(models.Model):
    criador = models.ForeignKey(
        "Usuario", on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='%(class)s_criado_por'
    )
    atualizado_por = models.ForeignKey(
        "Usuario", on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='%(class)s_atualizado_por'
    )
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Cidade(Auditoria):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.nome}/{self.estado}"


class Pessoa(Auditoria):
    primeiro_nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class Usuario(Auditoria):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    pessoa = models.OneToOneField(
        "Pessoa", verbose_name=("Pessoa"), on_delete=models.CASCADE)


class Dispositivos(Auditoria):
    descricao = models.CharField(max_length=30)
    data_instalacao = models.DateField(null=True, blank=True)
    ultima_manutencao = models.DateField(null=True, blank=True)
    
class Reles(Dispositivos):
    estaLigado = models.BooleanField()

class Sensor(Dispositivos):
    TIPO_SENSOR = (
        ("TEMPERATURA", "Temperatura"),
        ("UMIDADE", "Umidade"),
        ("PRESSAO", "Pressão"),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_SENSOR)

class Leitura(Auditoria):
    TIPO_LEITURA = (
        ("TEMPERATURA", "Temperatura"),
        ("UMIDADE", "Umidade"),
        ("PRESSAO", "Pressão"),
        # Adicione outros tipos de leitura conforme necessário
    )
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    tipo_leitura = models.CharField(max_length=20, choices=TIPO_LEITURA)
    valor = models.CharField(max_length=50)  # Valor armazenado como string para flexibilidade

    def __str__(self):
        return f"{self.sensor.descricao} - {self.tipo_leitura}: {self.valor}"

class Conexao(Auditoria):
    TIPO_CONEXAO = (
        ("MQTT", "MQTT"),
        ("RABBITMQ", "RabbitMQ"), 
        ("SERIAL", "Serial"),
    )
    descricao = models.CharField(max_length=30)
    tipo_conexao = models.CharField(max_length=20,
                                             choices=TIPO_CONEXAO,
                                             default="SERIAL")
     
    
class Microcontrolador(Auditoria):
    TIPO_CONTROLADOR = (
        ("ESP32","ESP32"),
        ("ARDUINO_UNO", "Arduino Uno"), 
        ("ARDUINO", "Arduino"), 
    )
    descricao = models.CharField(max_length=30)
    atual_codigo = models.TextField()
    tipo_microcontrolador = models.CharField(max_length=20,
                                    choices=TIPO_CONTROLADOR,
                                    default="ARDUINO")
    conexao = models.ForeignKey(Conexao, on_delete=models.CASCADE)
    
class Acessos(Auditoria):
    NIVEIS_ACESSO = (
        ("TOTAL", "Total"), 
        ("VISUALIZAR", "Visualizar"),
        ("ALTERAR_VISUALIZAR", "Alterar e Visualizar")
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)    
    microcontrolador = models.ForeignKey(Microcontrolador, on_delete=models.CASCADE)
    nivel_acesso = models.CharField(max_length=20,
                                    choices=NIVEIS_ACESSO,
                                    default="Total")
    
    