

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'pfmapp/home.html')