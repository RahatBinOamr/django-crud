from django.contrib import admin
from employee.models import Employee


class employeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'address')


admin.site.register(Employee, employeeAdmin)

# Register your models here.
