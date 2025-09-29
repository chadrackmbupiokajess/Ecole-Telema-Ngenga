from django.db import models

class SingletonModel(models.Model):
    """Modèle abstrait pour s'assurer qu'il n'y a qu'un seul objet."""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class APropos(SingletonModel):
    titre = models.CharField(max_length=200, default="À Propos de l'École Téléma Ngenga")
    contenu = models.TextField(blank=True)

    class Meta:
        verbose_name = "Page À Propos"

class NotreHistoire(SingletonModel):
    titre = models.CharField(max_length=200, default="Notre Histoire")
    contenu = models.TextField(blank=True)

    class Meta:
        verbose_name = "Page Notre Histoire"

class NotreMission(SingletonModel):
    titre = models.CharField(max_length=200, default="Notre Mission")
    contenu = models.TextField(blank=True)

    class Meta:
        verbose_name = "Page Notre Mission"
