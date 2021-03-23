from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import ScoreSheet, FileStoreage

@admin.register(ScoreSheet)
class ScoreSheetAdmin(ImportExportModelAdmin):
    pass

@admin.register(FileStoreage)
class FileStorageAdmin(ImportExportModelAdmin):
    pass