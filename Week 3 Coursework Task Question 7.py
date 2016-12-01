#Week 3
#Question 7

class primeNumber():
    """Function to check if a number given by the user is prime"""
    primeNumber = int(input("Can you please enter a prime number?"))#User gives a number
    #Prime numbers: 2,3,5,7,11,13,17,19,23,29,31,37,41,47,53

    if primeNumber == 0:
        print(primeNumber,"is not a prime number") #If it's not prime, this will print

    else:
        for i in range(1,primeNumber): #Check if number is prime
            if (primeNumber % i) == 0:
                print(primeNumber, "is a prime number") #If it's prime, this will print

primeNumber()
