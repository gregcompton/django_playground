from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("Are we getting here")
    return render(request, 'app/index.html')

