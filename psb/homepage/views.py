from django.shortcuts import render, redirect
from django.http import HttpResponse
from .support_functions import handle_uploaded_file
from DataManager.DataManager import DataManager
from psb.settings import BASE_DIR


def homepage(request):
    return render(request, "homepage/homepage.html", {})


def upload(request):
    if request.method == "POST":
        cfg_path = handle_uploaded_file(request.FILES['file'], request.FILES['file'].name)

        dm = DataManager()
        dm.save_photos(cfg_path, BASE_DIR + "/uploads/banners/")

    return redirect(homepage)

