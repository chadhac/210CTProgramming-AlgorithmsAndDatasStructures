#Week 4
#Question 9

class searching():
    """Function to do binary search"""
    user = int(input("Enter a number: "))
    number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    user = False
    a = 0
    b = len(number)+1 #Searching
    while a <= b and not user:
        c = (b+a)//2

        if user:
            print("Incorrect!") #Number is not in the list
        else:
            print("Correct!") #Number is in the list
