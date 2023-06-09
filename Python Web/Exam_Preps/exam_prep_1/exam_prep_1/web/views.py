from django.shortcuts import render

def index(request):
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
    return render(request, 'albums/profile-details.html')

def delete_profile(request):
    return render(request, 'albums/profile-delete.html')