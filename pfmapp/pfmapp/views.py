

from django.shortcuts import render, redirect

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'pfmapp/home.html')