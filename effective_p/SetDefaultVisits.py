class Visits: 
    def __init__(self):
        self.data= {}

    def add(self, country, city):
        """ still not idea. setdefault is still a confusing name. It also is not efficient, bc it constructs a new set instance on every call, regardless of whether the given country was already present in the data dictionary"""
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


