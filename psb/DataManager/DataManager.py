import pandas as pd
import requests
import numpy
from get.models import Banner

class DataManager():

    def __init__(self):
        pass

    def get_probability(self, x_i, x):
        return x_i / sum([i for i in x])

    def get_probabilities(self, x):
        return [self.get_probability(x_i, x) for x_i in x]

    def random_pick_from_given_distribution(self, objects, distr):
        _p = self.get_probabilities(distr) if distr != None else None
        return numpy.random.choice(objects, p=_p)

    def matching_values(self, a, b):
        return sum([1 if i in b else 0 for i in a])

    def save_data(self, cfg_path):
        ds = pd.read_csv(cfg_path, sep=";")

        for index, row in ds.iterrows():
            url = row[0]
            psa = row[1]
            cat_list = [row[i] for i in range(2, 11) if type(row[i]) == str]

            # DB object handling
            banner = Banner()
            banner.url = url
            banner.prepaid_shows_amount = psa
            banner.categories = ",".join(cat_list)
            banner.save()