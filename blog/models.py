from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class BlogPost(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    image_principale = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
