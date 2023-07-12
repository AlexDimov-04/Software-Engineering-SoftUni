import random
from django.shortcuts import render, redirect
from django.views.decorators import cache
from django.contrib.auth import get_user_model
from signals_middlewares_cache_session_demos.web.models import Task

UserModel = get_user_model()

@cache.cache_page(5 * 60)
def index(request):
    context = {
        'count': random.randrange(1, 1_000_000),
        'users': UserModel.objects.all()
    }

    return render(request, 'index.html', context=context)

def create_task(request):
    Task.objects.create(title=f'Title {random.randrange(1, 10_000)}')
    return redirect('index')
