'''
Created on 

Course work: 

@author: chaaya

Source:
     
     
'''

def weekday(x):
    if x == 1:
        day = "monday"
    elif x == 2:
        day = "tuesday"  
    elif x == 3:
        day = "wednesday"
    elif x == 4:
        day = "thursday"          
    elif x == 5:
        day = "friday"
    elif x == 6:
        day = "saturday"
    elif x == 7:
        day = "sunday"
    else:
        day = "error"         
    return day   

def startpy():

    user_input = int(input("enter a number for the week(1-7)"))
    week = weekday(user_input)
    print(week)   


if __name__ == '__main__':
    startpy()