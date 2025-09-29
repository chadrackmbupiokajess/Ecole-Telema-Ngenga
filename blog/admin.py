from django.contrib import admin
from django.db import models
from .models import BlogPost
from tinymce.widgets import TinyMCE

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    list_filter = ('date_publication', 'auteur')
    search_fields = ('titre', 'contenu')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(BlogPost, BlogPostAdmin)
