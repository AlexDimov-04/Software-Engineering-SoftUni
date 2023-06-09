from django import forms
from django.shortcuts import render
from forms_demos.web.models import Person

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=30)


def index(request):
    if request.method == 'GET':
        form = NameForm()
    else:
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(name=name)
    context = {
        'form': form,
        'name': name
    }

    return render(request, 'index.html', context=context)
