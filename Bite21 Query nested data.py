from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]

#these functions pass:

def get_all_jeeps(cars: CarsType = cars) -> str:
    if 'Jeep' in cars:
        return(', '.join(cars['Jeep']))
 
   
def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    list_of_first_cars = []
    for brand, cars_list in cars.items():
        list_of_first_cars.append(cars_list[0])
    return list_of_first_cars



def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    found_cars = []
    for brand, cars_list in cars.items():
        for car_type in cars_list:
            if grep.lower() in car_type.lower():
                found_cars.append(car_type)
    return found_cars  #if it is required to put them in alphabetical order, then 

def sort_car_models(cars: CarsType = cars) -> CarsType:
    alphabetized_cars_dict = {}
    for brand, cars_list in cars.items():
        alphabetized_cars_dict[brand] = sorted(cars_list)
    return alphabetized_cars_dict


