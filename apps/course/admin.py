from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", 'teacher']
    list_filter = ['name', 'teacher']
    search_fields = ['name', 'teacher']

admin.site.register(Course)
