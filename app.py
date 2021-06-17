'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
 


def remove_duplicates(city_list):

    non_duplicate_cities = []

    for x in city_list:
        if x not in non_duplicate_cities:
            non_duplicate_cities.append(x)
    return non_duplicate_cities

def startpy():

    c_list = [
        "Chennai",
        "Hyderabad",
        "Montreal",
        "Chennai",
        "Montreal"
    ]

    unique_cities = remove_duplicates(c_list)
   
    print(unique_cities)


if __name__ == '__main__':
    startpy()