'''
Created on 

Course work: 

@author: raja

Source:
     
     
'''
def get_age1(dict1):
    for i in dict1:
        #if type(i) == dict1 :
            print(i,dict1[i]) 


def startpy():
    nest_dict = {
        "name"      : "vedha",
        "list1"     : [1,2,3],
        "dict1"     : {
            "age"       :23,
            "age1"      :21
        },
        "list2"     : [4,5,6],
        "dict2"     : {
            "vedha"    :18,
            "age1"     :21
        }
    }
    
    get_age1(nest_dict)
   # print(nest_dict)
 


if __name__ == '__main__':
    startpy()