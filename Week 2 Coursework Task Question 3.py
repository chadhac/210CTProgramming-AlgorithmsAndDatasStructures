#Week 3
#Question 3

import math

class square():
    """This function will return the highest perfect positive square"""
    perfect = int(input("Enter a number: ")) #Ask user for input
    square = 0
    #Square numbers: 1,4,9,16,25,30,49,64,81,100
    
    if perfect >= 10: #square number algorithm
        while square*square < perfect:
            square = 10 + square
    if square*square != perfect: 
        print(perfect,"is a perfect square") #This will print if it's a perfect Square
    else:
        print(perfect,"is not a perfect square") #This will prin if it's not a perfect Square

square()

