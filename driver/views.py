from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def driver_dashboard(request):
    return render(request, 'driver/dashboard.html')


def test_page(request):
    return render(request, 'base.html')

