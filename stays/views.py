from django.shortcuts import render
from django.http import HttpResponse
from .models import LabUser


def index(request):
    return render(request,'index.html')


# Create your views here.
