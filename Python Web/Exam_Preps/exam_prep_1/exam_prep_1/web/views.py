from django.shortcuts import redirect, render
from exam_prep_1.web.models import Profile

def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None

def index(request):
    profile = get_profile()

    if profile is None:
        return redirect('add profile')

    return render(request, 'core/home-with-profile.html')

def add_album(request):
    return render(request, 'albums/add-album.html')

def details_album(request, pk):
    return render(request, 'albums/album-details.html')

def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')

def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')

def details_profile(request):
    return render(request, 'profiles/profile-details.html')

def add_profile(request):
    return render(request, 'core/home-no-profile.html')

def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')