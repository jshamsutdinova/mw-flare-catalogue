from django.contrib import admin
from catalogue.models import FlareList, Flare


@admin.register(FlareList)
class FlareListAdmin(admin.ModelAdmin):
    list_display = ['date', 'date_added']
    search_fields = ['date']
    ordering = ['-date']


@admin.register(Flare)
class FlareAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_event', 'finish_event',)
