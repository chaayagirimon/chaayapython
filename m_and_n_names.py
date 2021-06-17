'''
Created on 

Course work: 

@author: raja

Source:
     
     
'''

def return_specific_names(names):

    namelist = []
    for x in names:
        if x[0] == 'n' or x[0] == 'm':
            namelist.append(x)
    return namelist

def startpy():
    names = [
        "noor",
        "sam",
        "max",
        "manoj",
        "saneeth",
        "deeksha",
        "monty"
    ]

    name_list = return_specific_names(names) 
    print(name_list)  


if __name__ == '__main__':
    startpy()