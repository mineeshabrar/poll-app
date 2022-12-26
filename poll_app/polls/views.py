from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse - server provides the client with the resource it has requested

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")