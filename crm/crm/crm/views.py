from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

def home_view(request):
    return render(request, 'home.html')
