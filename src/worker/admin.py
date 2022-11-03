from django.contrib import admin

from .models import Departament, Employee


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('departament', 'surname')
    search_fields = ('name', 'surname')
