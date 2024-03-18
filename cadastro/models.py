from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome}"
    
    class Meta: 
        ordering = ["nome"]
    
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(max_length = 120,blank  = True, null= True)
    rede_social = models.URLField(max_length = 120,blank  = True, null= True,
                                  help_text="Passa o zap gasosa")
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    salario = models.DecimalField(verbose_name="Salário",decimal_places=2, max_digits=9)
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
    
    