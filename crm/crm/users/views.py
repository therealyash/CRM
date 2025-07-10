from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import CustomUserCreationForm  

@never_cache
@login_required
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            group = Group.objects.get(name=role)
            user.groups.add(group)
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@never_cache
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')
