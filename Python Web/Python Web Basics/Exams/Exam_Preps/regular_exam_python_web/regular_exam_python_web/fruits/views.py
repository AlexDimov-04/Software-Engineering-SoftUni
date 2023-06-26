from django.shortcuts import render, redirect
from regular_exam_python_web.fruits.models import Profile, Fruits
from regular_exam_python_web.fruits.forms import CreateProfileForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, EditProfileForm, DeleteProfileForm

def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, 'home/index.html', context=context)

def dashboard(request):
    fruits = Fruits.objects.all()
    profile = Profile.objects.first()

    context = {
        'fruits': fruits,
        'profile': profile
    }

    return render(request, 'dashboard/dashboard.html', context=context)

def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'form': form
    }

    return render(request, 'profiles/create-profile.html', context=context)

def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')
        
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/edit-profile.html', context=context)

def details_profile(request):
    profile = Profile.objects.first()
    fruits = Fruits.objects.count()

    context = {
        'profile': profile,
        'fruits_count': fruits
    }

    return render(request, 'profiles/details-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/delete-profile.html', context=context)

def create_fruit(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'fruits/create-fruit.html', context=context)

def details_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruits.objects.get(pk=pk)

    context = {
        'profile': profile,
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context=context)

def edit_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruits.objects.get(pk=pk)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'fruits/edit-fruit.html', context=context)

def delete_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruits.objects.get(pk=pk)

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'fruits/delete-fruit.html', context=context)