from django.shortcuts import render, redirect
from exam_prep_3.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, ProfileDeleteForm
from exam_prep_3.web.models import Profile, Car

def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }

    return render(request, 'base/index.html', context=context)

def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form
    }

    return render(request, 'profiles/profile-create.html', context=context)

def profile_details(request):
    profile = Profile.objects.first()
    total_price_cars = sum(car.price for car in Car.objects.all())

    context = {
        'profile': profile,
        'total_price': total_price_cars
    }

    return render(request, 'profiles/profile-details.html', context=context)

def profile_edit(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')
        
    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-edit.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context=context)

def catalogue(request):
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'cars': cars,
        'cars_count': cars_count
    }

    return render(request, 'catalogues/catalogue.html', context=context)

def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form
    }

    return render(request, 'cars/car-create.html', context=context)

def details_car(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
    }

    return render(request, 'cars/car-details.html', context=context)

def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form,
    }

    return render(request, 'cars/car-edit.html', context=context)

def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form,
    }

    return render(request, 'cars/car-delete.html', context=context)
