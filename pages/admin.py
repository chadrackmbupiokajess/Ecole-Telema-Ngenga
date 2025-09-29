from django.contrib import admin
from django.db import models
from .models import APropos, NotreHistoire, NotreMission
from tinymce.widgets import TinyMCE

class AProposAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class NotreHistoireAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class NotreMissionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(APropos, AProposAdmin)
admin.site.register(NotreHistoire, NotreHistoireAdmin)
admin.site.register(NotreMission, NotreMissionAdmin)
