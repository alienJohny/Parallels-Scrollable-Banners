from django.shortcuts import render, redirect
from django.http import HttpResponse
from DataManager.DataManager import DataManager
from get.models import Banner

def get(request):

    for obj in Banner.objects.order_by("prepaid_shows_amount"):
        print(obj.categories, obj.prepaid_shows_amount)

    if request.method == "GET":
        if "category" in request.GET:
            print(request.GET)

    return HttpResponse("get page")


