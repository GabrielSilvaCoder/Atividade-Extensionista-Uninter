from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20, blank=True, null=True)
    risco_eminente = models.BooleanField(default=False)
    descricao = models.TextField()
    nivel_agua = models.CharField(max_length=50, blank=True, null=True)  
    moradores_precisam_ajuda = models.BooleanField(default=False)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[("Aberto", "Aberto"), ("Em andamento", "Em andamento"), ("Resolvido", "Resolvido")],
        default="Aberto"
    )
    categoria = models.CharField(
        max_length=50,
        choices=[("Enchente", "Enchente"), ("Deslizamento", "Deslizamento"), ("Inundação leve", "Inundação leve")],
        default="Enchente"
    )
    prioridade = models.CharField(
        max_length=20,
        choices=[("Baixa", "Baixa"), ("Média", "Média"), ("Alta", "Alta")],
        default="Média"
    )
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    compartilhado = models.BooleanField(default=False)

    def __str__(self):
        return f"Relato de {self.rua}, {self.bairro} - {self.cidade}"
