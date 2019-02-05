from django.shortcuts import render, redirect
from django.http import HttpResponse
from .support_functions import handle_uploaded_file
from DataManager.DataManager import DataManager


def homepage(request):
    return render(request, "homepage/homepage.html", {})


def upload(request):
    if request.method == "POST":
        path = handle_uploaded_file(request.FILES['file'], request.FILES['file'].name)
    return redirect(homepage)

