from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Index route')

def random(request):
    return HttpResponse('Raddom route..')

def hello(request):
    return HttpResponse('Empty Rout..')



# Create your views here.
