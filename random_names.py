'''
Created on 

Course work: 

@author: raja

Source:
    
'''

from faker import Faker
 
fake=Faker()

def generate_random_names():

    random_names = []
    for x in range(5) :
        random_names.append(fake.name())
    return  random_names  
    

def startpy():

    random_name_list = generate_random_names()   
    print(random_name_list)


if __name__ == '__main__':
    startpy()