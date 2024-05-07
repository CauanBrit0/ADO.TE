from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import constants
from django.contrib import messages
from divulgar.models import Pet, Raca,Tag
from django.http import HttpResponse



def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status = 'P')
        racas = Raca.objects.all()
        raca_filter = request.GET.get('raca')
        cidade = request.GET.get('cidade')
        if cidade:
            pets = pets.filter(cidade__icontains = cidade)
        
        if raca_filter:
            pets = pets.filter(raca_id = raca_filter)
            raca_filter = Raca.objects.get(id = raca_filter)
        return render(request,'listar_pets.html',{'pets':pets, 'racas': racas,'raca_filter':raca_filter,'cidade':cidade })
    
