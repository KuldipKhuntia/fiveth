from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tofan(request):
    return HttpResponse('<h2>i love my india</h2>')