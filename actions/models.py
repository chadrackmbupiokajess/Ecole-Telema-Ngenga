from django.db import models
from django.urls import reverse

class ActionProject(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_realisation = models.DateField()
    image_principale = models.ImageField(upload_to='actions_photos/', help_text="Image principale de l'action.")
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('actions:action_detail', kwargs={'pk': self.pk})

class Testimonial(models.Model):
    texte = models.TextField()
    auteur = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text="Ex: Élève en 4ème année, Parent, Partenaire")
    projet_associe = models.ForeignKey(ActionProject, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Témoignage de {self.auteur}'

class GalleryImage(models.Model):
    projet = models.ForeignKey(ActionProject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    legende = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Image pour {self.projet.titre}'
