from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def index(request):
    alex = UserModel.objects.get(username='alex')

    context = {
        'user': alex
    }

    return render(request, 'index.html', context=context) 
