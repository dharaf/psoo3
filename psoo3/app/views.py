from django.shortcuts import render
from . models  import*

def consulta(request):
    consultas = {
         'consultas':pessoas.objects.all()
        }

    return render(request,'consulta/consulta.html',consultas)

