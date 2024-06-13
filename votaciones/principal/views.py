from django.shortcuts import render

# Create your views here.

from principal.models import Voto


def lista_votos(request):
    votos = Voto.objects.all()
    maximo = 0
    total = 0
    for elem in votos:
        total += elem.votos
        if elem.votos > maximo:
            maximo = elem.votos
    
    for elem in votos:
        elem.largo = int((elem.votos * 100) / maximo) - 10
    return render(request, 'grafico.html', {'lista': votos, 'totales': total})
    