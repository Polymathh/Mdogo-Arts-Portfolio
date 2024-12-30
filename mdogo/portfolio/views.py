from django.shortcuts import render, get_object_or_404, redirect
from .models import Cartoon
from django.contrib.auth import logout
from django.urls import path

# Create your views here.
def home(request):
    cartoons = Cartoon.objects.all()
    return render(request, 'home.html',{'cartoons': cartoons})


def cartoon_detail(request, pk):
    cartoon = get_object_or_404(Cartoon, pk=pk)
    return render(request, 'cartoon_detail.html', {'cartoon': cartoon})

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home')  