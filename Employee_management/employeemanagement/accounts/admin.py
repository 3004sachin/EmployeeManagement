from django.contrib import admin
from . models import *

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','employee_name','employee_profile','department','location','salary','bonus','role','phone','hire_date']

