from django.contrib import admin
from .models import Team, Publication, Conference, Presentation

# Register your models here.
admin.site.register(Team)
admin.site.register(Publication)
admin.site.register(Conference)
admin.site.register(Presentation)
