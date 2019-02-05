from django.db import models

class Banner(models.Model):
    url = models.URLField()
    prepaid_shows_amount = models.IntegerField()
    categories = models.TextField()
