'''
Created on 

Course work: 

@author: raja

Source:
     
     
'''

def get_merged_list(list1, list2):
    non_duplicates = []
    merged_list = list1 + list2
    for x in merged_list:
        if x not in non_duplicates:
            non_duplicates.append(x)
    return non_duplicates        
    

def startpy():

    list1 = ["jupiter","prakash","ram","raju","bruno",2.3]
    list2 = [2.3,"jupiter","mars","mercury","venus",134340,"saturn"]
    combined_list = get_merged_list(list1, list2)   
    print(combined_list)



if __name__ == '__main__':
    startpy()