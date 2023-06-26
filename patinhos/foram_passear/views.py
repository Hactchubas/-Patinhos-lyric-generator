from django.shortcuts import render, redirect
from num2words import num2words
from .patinhos import letra_gerador
# Create your views here.
def index(request):
    return render(request,"foram_passear/index.html")

def gerador(request):
    n_patinhos = request.GET.get('patinhos')
    if n_patinhos is not '':
        n_patinhos = int(n_patinhos)
        if n_patinhos <= 0:
            return render(request, "foram_passear/index.html",{
                "message": "Por favor insira um valor inteiro positivo"
            })
        letra = letra_gerador(n_patinhos)
        n_patinhos = num2words(n_patinhos,lang="pt_BR").capitalize()
        if n_patinhos != "Um": 
            n_patinhos += " patinhos"
        else:
            n_patinhos += " patinho"
        return render(request, "foram_passear/index.html",{
            "n_patinhos": n_patinhos,
            "letra": letra,
        })
    
    return render(request, "foram_passear/index.html",{
         "message": "Por favor insira um valor inteiro positivo"
    })
    
    