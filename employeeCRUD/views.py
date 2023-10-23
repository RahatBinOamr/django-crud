from django.shortcuts import render, redirect
from .forms import EmployeeFrom
from employee.models import Employee


def HomePage(request):
    form = EmployeeFrom()
    if request.method == "POST":
        form = EmployeeFrom(request.POST)
        form.save()
        return redirect('/')
    employeeData = Employee.objects.all()
    context = {
        'form': form,
        'employeeData': employeeData
    }
    return render(request, 'index.html', context)


def DeleteEmployee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def updateEmployee(request, id):
    if request.method == 'POST':
        data = Employee.objects.get(id=id)
        form = EmployeeFrom(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = Employee.objects.get(id=id)
    form = EmployeeFrom(instance=data)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)
