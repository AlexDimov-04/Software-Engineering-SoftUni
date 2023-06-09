from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http.response import Http404


def index(request):
    print(request)
    return HttpResponse("index")


def details(request, department_id):
    departments_map = {"1": "Developers", "2": "QA"}

    payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"
    # return HttpResponse(payload)
    # return redirect('/departments/template/', department_id=department_id)
    # return redirect('https:softuni.bg')
    return redirect("departments template", department_id=department_id)


def details_template(request, department_id):
    departments_map = {"1": "Developers", "2": "QA"}

    payload = f"Department: {departments_map.get(str(department_id), 'Unknown')}"

    context = {
        "title": "Na baba mi kaisiite",
        "payload": payload,
    }

    return render(request, "departments/details.html", context)


def details_error(request):
    raise Http404
