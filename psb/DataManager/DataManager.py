class DataManager():

    def __init__(self):
        pass

    def _get_probability(self, x_i, x):
        return x_i / sum([i for i in x])

    def get_probabilities(self, x):
        return [self._get_probability(x_i, x) for x_i in x]

    def matching_values(self, a, b):
        return sum([1 if i in b else 0 for i in a])

