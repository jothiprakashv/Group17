from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin):
    pass