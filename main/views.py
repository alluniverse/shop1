from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

