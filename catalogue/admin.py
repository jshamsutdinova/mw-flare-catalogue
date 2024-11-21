from django.contrib import admin
from catalogue.models import YearMonth, SummaryDay

# Register your models here.

class CatalogueAdmin(admin.ModelAdmin):
    pass

admin.site.register(YearMonth, CatalogueAdmin)
admin.site.register(SummaryDay, CatalogueAdmin)
