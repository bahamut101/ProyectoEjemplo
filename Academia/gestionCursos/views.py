from django.shortcuts import render

# Create your views here.

def buscaCursos(request):
    return render(request, "buscaCursos.html")