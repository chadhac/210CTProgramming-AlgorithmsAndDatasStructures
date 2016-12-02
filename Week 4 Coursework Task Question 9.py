#Week 4
#Question 9

def searching(user,number):
    """Function to do binary search"""
    user = int(input("Enter a number: "))
    number = [0,1,2,3,4,5,6,7,8,9,10]
    found = searching(user, number)
    if found:
        print("Incorrect!")
    else:
        print("Correct!")

        if number[middle]==user:
            found = True
        else number[middle] < user:
            bottom = middle + 1

searching()
