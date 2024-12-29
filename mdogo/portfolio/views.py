from django.shortcuts import render, get_object_or_404
from .models import Cartoon


# Create your views here.
def home(request):
    cartoons = Cartoon.objects.all()
    return render(request, 'home.html',{'cartoons': cartoons})


def cartoon_detail(request, pk):
    cartoon = get_object_or_404(Cartoon, pk=pk)
    return render(request, 'cartoon_detail.html', {'cartoon': cartoon})