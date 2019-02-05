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
        return numpy.random.choice(objects, p=self.get_probabilities(distr))

    def matching_values(self, a, b):
        return sum([1 if i in b else 0 for i in a])

    def to_csv(self, l):
        return ",".join(l)

    def from_csv(self, s):
        return s.split(",")

    def download_photo(self, url, destination):
        img_name = url.split("/")[-1]
        path_to_image = destination + img_name
        with open(path_to_image, 'wb') as f:
            f.write(requests.get(url).content)

        return path_to_image

    def save_photos(self, cfg_path, img_path):
        ds = pd.read_csv(cfg_path, sep=";")

        for index, row in ds.iterrows():
            url = row[0]
            psa = row[1]
            cat_list = [row[i] for i in range(2, 11) if type(row[i]) == str]

            path_to_image = self.download_photo(url, img_path)

            # DB object handling
            banner = Banner()
            banner.image = path_to_image
            banner.url = url
            banner.prepaid_shows_amount = psa
            banner.categories = ",".join(cat_list)
            banner.save()