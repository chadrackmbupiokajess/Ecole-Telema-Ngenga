from django.db import models
from django.conf import settings

class TeamMember(models.Model):
    CATEGORIES = (
        ('terrain', 'Sur le terrain'),
        ('coulisses', 'Dans les coulisses'),
    )

    nom = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.nom

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        # Retourne l'URL d'une icône SVG d'avatar par défaut
        return "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%23a0aec0'%3E%3Cpath fill-rule='evenodd' d='M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z' clip-rule='evenodd' /%3E%3C/svg%3E"
