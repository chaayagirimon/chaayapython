'''
Created on 

Course work: 

@author: raja

Source:
     
     
'''

def dict_to_list(age_dict):

    age_list = list(age_dict.values())
    return age_list

def startpy():
    age_dict = {
       "vedha"      : 18,
       "deeksha"    : 21,
       "saneeth"    : 25,
       "vasavi"     : 21,
       "harsha"     : 21,
       "chaaya"     : 19
    }

    age_list = dict_to_list(age_dict)   
    print(age_list)

if __name__ == '__main__':
    startpy()