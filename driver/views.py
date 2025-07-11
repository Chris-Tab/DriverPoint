from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import DriverProfile
from .forms import DriverProfileForm


@login_required
def driver_dashboard(request):
    return render(request, 'driver/dashboard.html')


@login_required
def driver_profile(request):
    try:
        profile = DriverProfile.objects.get(user=request.user)
    except DriverProfile.DoesNotExist:
        return redirect('driver:create_profile')
    return render(request, 'driver/profile.html', {'profile': profile})


@login_required
def create_driver_profile(request):
    if DriverProfile.objects.filter(user=request.user).exists():
        return redirect('driver:profile')

    if request.method == 'POST':
        form = DriverProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('driver:profile')
    else:
        form = DriverProfileForm()

    return render(request, 'driver/create_profile.html', {'form': form})


@login_required
def edit_driver_profile(request):
    try:
        profile = DriverProfile.objects.get(user=request.user)
    except DriverProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = DriverProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('driver:profile')
    else:
        form = DriverProfileForm(instance=profile)

    return render(request, 'driver/edit_profile.html', {'form': form})
