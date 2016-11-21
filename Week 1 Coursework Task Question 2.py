#Question 2
#Number of trailing 0s in a fatorial number
#http://www.programiz.com/python-programming/examples/factorial

#To get a different result, please change the value
number = 4
number = int(input("Can you please enter a number?"))
factorial = 1

if number < 0: #Check if the number is negative, positive or zero
   print("It doesn't exist for negative numbers")
elif number == 0:
   print("Factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("Factorial",number,"is",factorial)
