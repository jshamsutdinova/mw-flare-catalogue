from django.contrib import admin
from catalogue.models import Flare


@admin.register(Flare)
class FlareAdmin(admin.ModelAdmin):
    list_display = ['date', 'start_event', 'end_event', 'updated']
    list_filter  = ['tag']
