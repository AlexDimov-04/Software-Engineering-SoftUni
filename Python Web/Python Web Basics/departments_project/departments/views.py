from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    print(request)
    return HttpResponse('index')


def details(request, department_id):
    departments_map = {
        '1': "Developers",
        '2': "QA"
    }

    payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"
    # return HttpResponse(payload)
    # return redirect('/departments/template/', department_id=department_id)
    return 

def details_template(request, department_id):
    departments_map = {
        '1': "Developers",
        '2': "QA"
    }

    payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"

    context = {
        'title': 'Na baba mi kaisiite',
        'payload': payload,
    }

    return render(request, 'departments/details.html', context)

    