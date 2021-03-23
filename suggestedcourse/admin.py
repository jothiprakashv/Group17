from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from suggestedcourse.models import SuggestedCourse



@admin.register(SuggestedCourse)
class SuggestedCourseAdmin(ImportExportModelAdmin):
    pass