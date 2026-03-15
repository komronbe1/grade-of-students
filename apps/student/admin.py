from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", 'last_name', 'phone', 'email']
    list_filter = ["first_name", 'last_name', 'phone', 'email']
    search_fields = ["first_name", 'last_name', 'phone', 'email']

admin.site.register(Student, StudentAdmin)
