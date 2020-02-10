from django import forms
from .models import Servicos, Imagens, Parceiros
from phone_field import PhoneField

class ParceirosForm(forms.ModelForm):
    class Meta:
        prefix = 'parceiro'
        model = Parceiros
        fields = ['nome', 'endereco', 'responsavel', 'tel']
    


class ServicosForm(forms.ModelForm):
    tipo = forms.CharField(max_length=200)
    objetivo = forms.CharField(max_length=500)
    preco = forms.DecimalField(max_digits=9, decimal_places=2)
    telefone = PhoneField(max_length=12)

    class Meta:
        prefix = 'service'
        model = Servicos
        fields = ['tipo', 'objetivo', 'preco', 'telefone']


class ImagensForm(forms.ModelForm):
    imagem = forms.ImageField(label='image')

    class Meta:
        model = Imagens
        fields = ['imagem']


