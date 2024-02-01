from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def tennis(request):
    return HttpResponse("This is the tennis app.")
