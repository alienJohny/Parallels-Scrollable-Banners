from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def get(request):
    return HttpResponse("get page")