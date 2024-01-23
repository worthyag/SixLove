from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    return HttpResponse("<h1>Hello Frontend</h1>")


def tennis(request, *args, **kwargs):
    return render(request, "tennis.html")
