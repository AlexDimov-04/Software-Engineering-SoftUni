from django.shortcuts import render
from .models import Employee

def index(request):

    employee = Employee.objects.all()
    print(employee)

    return render(request, 'web/index.html')