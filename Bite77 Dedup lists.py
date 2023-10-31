



my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']


def uncommon_cities(my_cities, other_cities):
    return len([city for city in my_cities if city not in other_cities] + [city for city in other_cities if city not in my_cities])