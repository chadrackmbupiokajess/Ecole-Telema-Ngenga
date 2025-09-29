from django.shortcuts import render
from .models import TeamMember

def equipe_view(request):
    membres_terrain = TeamMember.objects.filter(categorie='terrain')
    membres_coulisses = TeamMember.objects.filter(categorie='coulisses')
    context = {
        'membres_terrain': membres_terrain,
        'membres_coulisses': membres_coulisses,
    }
    return render(request, 'equipes.html', context)
