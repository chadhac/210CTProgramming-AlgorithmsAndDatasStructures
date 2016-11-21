#Week 2
#Question 3
#http://stackoverflow.com/questions/1547196/finding-perfect-square

def square(self, a):
    """This function will return the highest perfect square"""
    answer = a
    if a >= 0:
        while answer*answer < a:
            answer = answer + 1

        if answer*answer != a:
            print(a,"is not a square") #Not a square
            return None
        else:
            print(a,"is a square") #Is a square
            return answer
    else:
        print(a,"is not a positive number")
        return None

a = 20 #CHANGE this to get for a different value and it will tell you if it's a square e.g. 9 is a square but 15 isn't          
print(square(a,a)) #This will also print how and why it's a square number e.g. 25 is a square because 5
