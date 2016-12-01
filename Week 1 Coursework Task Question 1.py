#Week1
#Question 1

from random import shuffle #Random shuffle function

class number():
    """This function will randomly shuffle numbers between 0-9"""
    number = ['0','1','2','3','4','5','6','7','8','9'] #list
    number = [i for i in range(10)] #range
    shuffle(number)
    print(number) #print function

number()
