from django.forms import ModelForm
from employee.models import Employee
from django import forms


class EmployeeFrom(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'email': forms.TextInput({'class': 'form-control'}),
            'position': forms.TextInput({'class': 'form-control'}),
            'address': forms.TextInput({'class': 'form-control'})
        }
