#Week 1
#Question 2

class trailingFactorial():
    """Function to check number of trailing 0s in a factorial""" #Number of trailing 0s in a factorial number
    factorial = int(input("Can you please enter a number?")) #Ask user for number
    trailingFactorial = 1

    for i in range(1, factorial): #Trailing factorial algorithm
        trailingFactorial = i*trailingFactorial
        print("Factorial",factorial,"is",trailingFactorial) 
        
trailingFactorial()
