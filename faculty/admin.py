from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(ImportExportModelAdmin):
    pass