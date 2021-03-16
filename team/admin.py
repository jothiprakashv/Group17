from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Team

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    pass