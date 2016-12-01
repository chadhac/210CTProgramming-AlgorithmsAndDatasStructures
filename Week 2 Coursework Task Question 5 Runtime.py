#Week 2
#Question 5

import timeit
start = timeit.default_timer()

class matrice():
    """This function I will use pseudocode to function for addition, subtraction and multiplication"""
    n = 5  #Change value for different response
    b = 89 #Same as above
    c = 49 #Same as above
    n = b*c-2*(b+c)
    print(n)
   
matrice()

stop = timeit.default_timer()
print(stop - start)
