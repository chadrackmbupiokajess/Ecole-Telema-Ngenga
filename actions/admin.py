from django.contrib import admin
from django.db import models
from .models import ActionProject, Testimonial, GalleryImage
from tinymce.widgets import TinyMCE

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1  # Combien de champs de galerie vides afficher

class ActionProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_realisation')
    inlines = [GalleryImageInline]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'role', 'projet_associe')
    list_filter = ('projet_associe',)

admin.site.register(ActionProject, ActionProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
