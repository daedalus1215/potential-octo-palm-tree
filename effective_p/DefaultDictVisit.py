from collections import defaultdict


class Visits:
    def __init__(self) -> None:
        self.data = defaultdict(set)

    def add(self, country, city):
        """ Short and simple. This assumes that accessing any key in the data dictionary will always result in an existing set instance. No need to call set() which could be costly if the add method is called a large number of times. """
        self.data[country].add(city)
