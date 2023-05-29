from django.shortcuts import render, HttpResponse
from api import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the login index.")
    # return render(request, 'index.html')
