from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Giri(request):
    return HttpResponse('Hi kranthi how r u')
def kranthi(request):
    return HttpResponse('Hi giri I am fine u')