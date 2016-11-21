#Week1
#Question 1
#http://stackoverflow.com/questions/976882/shuffling-a-list-of-objects-in-python

from random import shuffle #Random shuffle function

def number():
    """This function will randomly shuffle numbers between 0-9"""
    number = ['0','1','2','3','4','5','6','7','8','9'] #list
    number = [i for i in range(10)] #range
    shuffle(number)
    print(number) #print function

number()
