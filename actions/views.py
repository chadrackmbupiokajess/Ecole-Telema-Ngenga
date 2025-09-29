from django.shortcuts import render, get_object_or_404, redirect
from .models import ActionProject, Testimonial
from django.db.models import F

# Vue pour la liste des actions
def action_list(request):
    # On utilise prefetch_related pour optimiser le chargement des images de la galerie
    projets = ActionProject.objects.prefetch_related('images').order_by('-date_realisation')
    temoignages = Testimonial.objects.all()
    context = {
        'projets': projets,
        'temoignages': temoignages,
    }
    return render(request, 'actions.html', context)

# Vue pour le détail d'une action
def action_detail(request, pk):
    project = get_object_or_404(ActionProject, pk=pk)

    # Logique pour le compteur de vues unique par session
    viewed_actions = request.session.get('viewed_actions', [])
    if project.pk not in viewed_actions:
        project.views = F('views') + 1
        project.save()
        viewed_actions.append(project.pk)
        request.session['viewed_actions'] = viewed_actions

    # Logique pour le "like" unique par session
    liked_actions = request.session.get('liked_actions', [])
    if request.method == 'POST':
        if project.pk not in liked_actions:
            project.likes = F('likes') + 1
            project.save()
            liked_actions.append(project.pk)
            request.session['liked_actions'] = liked_actions
        return redirect('actions:action_detail', pk=project.pk)

    # Recharger l'objet pour avoir les dernières valeurs
    project.refresh_from_db()

    # Récupérer les images de la galerie pour ce projet
    gallery_images = project.images.all()

    context = {
        'project': project,
        'gallery_images': gallery_images,
        'has_liked': project.pk in liked_actions
    }
    return render(request, 'action_detail.html', context)
