from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tag, Raca, Pet
from django.contrib.messages import constants
from django.contrib import messages


def novo_pet(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        raca = Raca.objects.all()
        return render(request, 'novo_pet.html',{'tags':tags,'raca':raca})
    
    if request.method =="POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or len(estado.strip()) == 0 or len(cidade.strip()) == 0 or len(telefone.strip()) == 0:
            messages.add_message(request,constants.INFO,'Preencha todos os campos.')
            return redirect('/divulgar/novo_pet/')
        
        if not foto:
            messages.add_message(request,constants.INFO,'Envie uma foto, para finalizar o cadastro do Pet!')
            return redirect('/divulgar/novo_pet/')
        
        if not tags:
            messages.add_message(request,constants.INFO,'Selecione ao menos uma tag ao seu Pet!')
            return redirect('/divulgar/novo_pet/')

        pet = Pet( usuario = request.user ,nome = nome, descricao = descricao, estado = estado, cidade = cidade, telefone = telefone, raca_id = raca, foto = foto)
        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id = tag_id)
            pet.tags.add(tag)
        
        pet.save()

        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'novo_pet.html',{'tags':tags, 'racas':racas})

