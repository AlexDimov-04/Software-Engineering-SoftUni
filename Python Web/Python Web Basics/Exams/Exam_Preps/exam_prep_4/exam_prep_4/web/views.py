from django.shortcuts import render, redirect
from exam_prep_4.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, ProfileDeleteForm
from exam_prep_4.web.models import Profile, Game

def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    return render(request, 'home/home-page.html', context=context)

def dashboard(request):
    games = Game.objects.all()
    profile = Profile.objects.first()

    context = {
        'games': games,
        'profile': profile
    }

    return render(request, 'dashboard/dashboard.html', context=context)

def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {'form': form}

    return render(request, 'profiles/create-profile.html', context=context)

def details_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.count()
    if games:
        average_rating = sum(game.rating for game in Game.objects.all()) / games
    else:
        average_rating = 0.0

    context = {'profile': profile, 'games_count': games, 'average_rating': average_rating}

    return render(request, 'profiles/details-profile.html', context=context)

def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')
        
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context=context)

def create_game(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'games/create-game.html', context=context)

def details_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)

    context = {
        'game': game,
        'profile': profile
    }

    return render(request, 'games/details-game.html', context=context)

def edit_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'games/edit-game.html', context=context)

def delete_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'games/delete-game.html', context=context)

