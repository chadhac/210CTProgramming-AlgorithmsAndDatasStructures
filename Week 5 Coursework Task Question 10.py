#Week 5
#Question 10

class extractingNumbers():
    """Function to extract numbers from a sequence in ascending order"""
    numbers = ["5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60"]
    numbers.remove("5")
    numbers.remove("10")
    numbers.remove("15")
    numbers.remove("20")
    numbers.remove("25")
    numbers.remove("30")
    print("Extracted list:", numbers)

extractingNumbers()
