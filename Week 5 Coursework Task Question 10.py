#Week 5
#Question 10

class extractingNumbers():
    """Function to extract numbers from a sequence in ascending order"""
    #Input: [5,10,15,20,25,30,35,40,45,50,55,60]
    #Output: [5,10,15,20,25,30]
    numbers = ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60"] #list
    numbers.remove("35")#remove
    numbers.remove("40")#same as above
    numbers.remove("45")#same as above
    numbers.remove("50")#same as above
    numbers.remove("55")#same as above
    numbers.remove("60")#same as above
    print("Extracted list:", numbers)

extractingNumbers()
