from django.contrib import admin
from .models import Team, Publication, Conference, Presentation, Proceedings


admin.site.register(Team)
admin.site.register(Publication)

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    pass

@admin.register(Presentation)
class PresentatationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'conf', 'first_author']
    list_filter = ['type', 'first_author', 'conf']


admin.site.register(Proceedings)
