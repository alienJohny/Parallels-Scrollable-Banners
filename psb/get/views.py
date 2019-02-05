from django.shortcuts import render, redirect
from django.http import HttpResponse
from DataManager.DataManager import DataManager
from get.models import Banner

def get(request):
    if request.method == "GET":
        if "category" in request.GET:
            categories = request.GET["category"]

            dm = DataManager()
            good_pks = []

            for obj in Banner.objects.order_by("-prepaid_shows_amount"):
                # If at least one category matches
                if dm.matching_values(obj.categories.split(","), categories) > 0:
                    # Save his database primary key
                    good_pks.append(obj.pk)

            sorted_psa = [Banner.objects.get(pk=good_pk).prepaid_shows_amount
                          for good_pk in good_pks]

            # Banner to be shown
            banner_pk = dm.random_pick_from_given_distribution(good_pks, sorted_psa)

            # Decrement amount of shows
            b = Banner.objects.get(pk=banner_pk)
            b.prepaid_shows_amount -= 1
            b.save()

    return HttpResponse("get page")


