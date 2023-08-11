from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()   #data is a list of dictionaries

#print(data)

def most_prolific_automaker(year):
    automakers = [dictionaries['automaker'] for dictionaries in data if dictionaries['year'] == year]
    automaker_count = Counter(automakers)
    #return automaker_cou
    name, count = automaker_count.most_common(1)[0]
    return name


    
    #return most_common_automaker()
    '''
    for dictionaries in data:
        if 'year' in dictionaries and dictionaries['year'] == year:
            automakers.append(dictionaries['automaker'])
    
    '''
    #return automakers
    #    return automaker_count
    
    #

     
print(most_prolific_automaker(1993))

'''        
    automaker_totals_list = [item['automaker'] for item in data]


    
'''


# print(automaker_totals_list)
#print(most_common_automaker)


        
            




# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    pass


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    pass