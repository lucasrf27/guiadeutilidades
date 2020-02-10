from django.contrib import admin
from .models import Parceiros, Servicos, Imagens

class ParceirosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'responsavel', 'tel', 'created_at', 'updated_at')

class ServicosAdmin(admin.ModelAdmin):
    list_display = ('parceiro', 'preco', 'telefone', 'objetivo', 'tipo')

class ImagensAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'imagem')


admin.site.register(Parceiros, ParceirosAdmin),
admin.site.register(Servicos, ServicosAdmin),
admin.site.register(Imagens, ImagensAdmin),