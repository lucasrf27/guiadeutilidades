from django.db import models
from phone_field import PhoneField
from datetime import datetime
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


User = get_user_model()

class Parceiros (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.TextField(max_length=400, blank=True)
    responsavel = models.CharField(max_length=100)
    tel = PhoneField(max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    ativo = models.BooleanField(default=False)

class Servicos (models.Model):
    tipo = models.CharField(max_length=200)
    objetivo = models.TextField(max_length=500, blank=True)
    parceiro = models.ForeignKey(Parceiros, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    telefone = PhoneField(max_length=12, default='21968151502')

def get_image_filename(instance, filename):
    tipo = instance.services.tipo
    slug = slugify(tipo)
    return "servicos_imagens/%s-%s" % (slug, filename)

class Imagens (models.Model):
    servicos = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=get_image_filename)
