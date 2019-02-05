import pandas as pd
import numpy
import json
from get.models import Banner

class DataManager():

    def __init__(self):
        self.prev_id_file_name = "DataManager/previousBannerId.json"

    def random_pick_from_given_distribution(self, objects, distr):
        """
        Selects a random object in accordance with a specified
        probability distribution of random variables.

        :param objects: Array of objects
        :param distr: Array, probability distribution
        :return: QueryDict object
        """
        _p = self._get_probabilities(distr) if distr != None else None
        return numpy.random.choice(objects, p=_p)

    def matching_values(self, a, b):
        """
        Counts the number of matching elements in two arrays of the same length.

        :param a: Array
        :param b: Array
        :return: Int
        """
        return sum([1 if i in b else 0 for i in a])

    def save_data(self, cfg_path):
        """
        Saves the configuration file to database.

        :param cfg_path: Config path
        :return: None
        """
        try:
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
        except:
            raise IOError

    def was_used(self, banner_pk, matching_pks):
        """
        Returns a new banner index from the list of available banners
        with a probability of 33% if the banner was shown earlier,
        otherwise it returns the same index.

        :param banner_pk: Banner to be shown index
        :param matching_pks: Available indexes
        :return: Int
        """

        # Only in 33% of cases repeating value will be changed
        if self._used_previously(banner_pk) and numpy.random.choice([0, 0, 1], 1):
            new_banner_pk = numpy.random.choice(matching_pks, 1)

            # Set new previous pk
            self._dump_new_prev_id(new_banner_pk)

            return new_banner_pk

        return banner_pk

    def _get_probability(self, x_i, x):
        return x_i / sum([i for i in x])

    def _get_probabilities(self, x):
        return [self._get_probability(x_i, x) for x_i in x]

    def _dump_new_prev_id(self, new_prev_id):
        with open(self.prev_id_file_name) as data_file:
            data = json.load(data_file)

        data["prevId"] = new_prev_id

        with open(self.prev_id_file_name, 'w') as outfile:
            json.dump(data, outfile)

    def _get_prev_id(self):
        with open(self.prev_id_file_name) as data_file:
            data = json.load(data_file)
        return data["prevId"]

    def _used_previously(self, banner_pk):
        if banner_pk == self._get_prev_id():
            return True
        return False
