from django.contrib import admin
from .models import Grade

class GradeAdmin(admin.ModelAdmin):
    list_display = ["student", 'course', 'grade']
    list_filter = ['student', 'course', 'grade']
    search_fields = ['course', 'student']

admin.site.register(Grade, GradeAdmin)