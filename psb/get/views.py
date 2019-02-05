from django.shortcuts import render, redirect
from django.http import HttpResponse
from DataManager.DataManager import DataManager
from get.models import Banner

def get(request):
    if request.method == "GET":

        # To manage the issuance of banners
        dm = DataManager()

        if "category" in request.GET:
            categories = request.GET["category"]
            good_pks = []

            # We do not show banners that have run out of paid shows
            for obj in Banner.objects.order_by("-prepaid_shows_amount").filter(prepaid_shows_amount__gt=0):
                # If at least one category matches
                if dm.matching_values(obj.categories.split(","), categories) > 0:
                    # Save his database primary key
                    good_pks.append(obj.pk)

            sorted_psa = [Banner.objects.get(pk=good_pk).prepaid_shows_amount
                          for good_pk in good_pks]

            # Banner to be shown
            banner_pk = dm.random_pick_from_given_distribution(good_pks, sorted_psa)

            # Decrement amount of shows
            banner_to_show = Banner.objects.get(pk=banner_pk)
            banner_to_show.prepaid_shows_amount -= 1
            banner_to_show.save()
        else:
            # Pick random banner
            banners = Banner.objects.filter(prepaid_shows_amount__gt=0)
            banner_to_show = dm.random_pick_from_given_distribution(banners, None)
            banner_to_show.prepaid_shows_amount -= 1
            banner_to_show.save()

    return render(request, 'get/get.html', {"banner_url": banner_to_show.url})

