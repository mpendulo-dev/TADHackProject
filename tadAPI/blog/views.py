from django.shortcuts import render

from django.shortcuts import render
from .models import CareerInfo

# Create your views here.

def main(request):
    context={'Posts':CareerInfo.objects.all()}
    return render(request, "blog/home.html", context)