from django.shortcuts import render, redirect
from django.http import HttpResponse
from .support_functions import handle_uploaded_file


def homepage(request):
    return render(request, "homepage/homepage.html", {})


def upload(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file'], request.FILES['file'].name)
    return redirect(homepage)

