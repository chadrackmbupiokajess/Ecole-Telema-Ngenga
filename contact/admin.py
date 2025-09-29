from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'nom', 'email', 'date_envoi')
    list_filter = ('date_envoi',)
    search_fields = ('nom', 'email', 'sujet', 'message')
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'date_envoi') # Rend les messages non-modifiables

admin.site.register(ContactMessage, ContactMessageAdmin)
