from django.shortcuts import render, redirect
from .models import Servicos, Parceiros, Imagens
from django.views.generic import UpdateView, DetailView, ListView
from .forms import ParceirosForm, ServicosForm, ImagensForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.context_processors import auth



def home_view(request):
    serv = Servicos.objects.all()
    context = {'serv': serv }
    return render (request, 'home.html', context)


@login_required
def parceiros_create(request):
    if request.method =='POST':
        form = ParceirosForm(request.POST)
        Parceiros.user = auth.user
        if form.is_valid():
            parceiro = form.save(commit=False)
            parceiro.save()
        return redirect('home2')
    else:
        form = ParceirosForm()
    context = {
        'form': form,
    }
    return render (request, 'parceiroform.html', context)


def parceirosview(request):
    user = Servicos.parceiro
    serv = Servicos.objects.get(parceiro=user)
    context = {'serv': serv}
    return render(request, 'parceiro.html', context)


class ServicoView(DetailView):
    model = Servicos



class ServicoUpdate(UpdateView):
    model = Servicos
    template_name = 'servicoform.html'

    