from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Course

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass