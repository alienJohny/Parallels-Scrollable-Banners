import pandas as pd
import requests

class DataManager():

    def __init__(self):
        pass

    def _get_probability(self, x_i, x):
        return x_i / sum([i for i in x])

    def get_probabilities(self, x):
        return [self._get_probability(x_i, x) for x_i in x]

    def matching_values(self, a, b):
        return sum([1 if i in b else 0 for i in a])

    def to_csv(self, l):
        return ",".join(l)

    def from_csv(self, s):
        return s.split(",")

    def download_photo(self, url, destination):
        img_name = url.split("/")[-1]
        with open(destination + img_name, 'wb') as f:
            f.write(requests.get(url).content)

    def save_photos(self, cfg_path, img_path):
        ds = pd.read_csv(cfg_path, sep=";")
        url_col = ds.columns[0]
        urls = ds[url_col]

        for url in urls:
            self.download_photo(url, img_path)
