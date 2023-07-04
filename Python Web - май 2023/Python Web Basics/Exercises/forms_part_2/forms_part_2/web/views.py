from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from forms_part_2.web.validators import validate_priority, validate_text, ValueInRangeValidator
from forms_part_2.web.forms import ToDoCreateForm

def index(request):
    if request.method == 'GET':
        form = ToDoCreateForm()
    else:
        form = ToDoCreateForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')
    
    context = {
        'form': form
    }

    return render(request, 'index.html', context=context)
