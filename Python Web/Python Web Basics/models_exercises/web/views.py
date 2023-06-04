from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee, Department

def index(request):
    context = {
        'employees': list(Employee.objects.all()),
        'filtered': Employee.objects.filter(department__name='Surgeon')
    }

    return render(request, 'web/index.html', context=context)

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')