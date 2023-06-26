from django.shortcuts import render, redirect
from exam_prep_2.web.forms import ProfileForm, PlantForm, PlantDeleteForm, PlantEditForm, ProfileEditForm, ProfileDeleteForm
from exam_prep_2.web.models import Profile, Plant

def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, 'home/home-page.html', context=context)

def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form
    }

    return render(request, 'profiles/create-profile.html', context=context)

def details_profile(request):
    profile = Profile.objects.first()
    plants_count = Plant.objects.count()

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profiles/profile-details.html', context=context)

def edit_profile(request):
    profile = Profile.objects.get()

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

    return render(request, 'profiles/edit-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'profiles/delete-profile.html', context=context)

def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants,
    }

    return render(request, 'catalogues/catalogue.html', context=context)

def create_plant_page(request):
    if request.method == 'GET':
        form = PlantForm()
    else:
        form = PlantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form
    }

    return render(request, 'plants/create-plant.html', context=context)

def details_plant_page(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {
        'plant': plant,
    }

    return render(request, 'plants/plant-details.html', context=context)

def edit_plant_page(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        
    context = {
        'form': form
    }

    return render(request, 'plants/edit-plant.html', context=context)

def delete_plant_page(request, pk):
    plant = Plant.objects.get(pk=pk)

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plants/delete-plant.html', context)


