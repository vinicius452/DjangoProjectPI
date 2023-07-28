from django.shortcuts import get_object_or_404, redirect, render

from .forms import CelularForm
from .models import Celular


def lista_celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'celulares/lista_celulares.html', {'celulares': celulares})

def detalhe_celular(request, celular_id):
    celular = get_object_or_404(Celular, pk=celular_id)
    return render(request, 'celulares/detalhe_celular.html', {'celular': celular})

def novo_celular(request):
    if request.method == 'POST':
        form = CelularForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_celulares')
    else:
        form = CelularForm()
    return render(request, 'celulares/novo_celular.html', {'form': form})

def editar_celular(request, celular_id):
    celular = get_object_or_404(Celular, pk=celular_id)
    if request.method == 'POST':
        form = CelularForm(request.POST, request.FILES, instance=celular)
        if form.is_valid():
            form.save()
            return redirect('lista_celulares')
    else:
        form = CelularForm(instance=celular)
    return render(request, 'celulares/editar_celular.html', {'form': form})

def excluir_celular(request, celular_id):
    celular = get_object_or_404(Celular, pk=celular_id)
    celular.delete()
    return redirect('lista_celulares')
