import os
from email.mime.image import MIMEImage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse

# Import des modèles des autres applications
from equipe.models import TeamMember
from actions.models import ActionProject, Testimonial
from blog.models import BlogPost

# Import des modèles locaux
from .models import APropos, NotreHistoire, NotreMission

# Import des formulaires
from contact.forms import ContactForm

# Vues pour les pages
def accueil(request):
    latest_posts = BlogPost.objects.order_by('-date_publication')[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'accueil.html', context)

def a_propos(request):
    page_content = APropos.load()
    return render(request, 'a-propos.html', {'page': page_content})

def histoire(request):
    page_content = NotreHistoire.load()
    return render(request, 'histoire.html', {'page': page_content})

def mission(request):
    page_content = NotreMission.load()
    return render(request, 'mission.html', {'page': page_content})

# Vue pour le fichier robots.txt
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
