from django.contrib import admin
from .models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('nom', 'role', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom', 'role', 'bio')

admin.site.register(TeamMember, TeamMemberAdmin)
