from math-funcs import addition, subtract, divide, multiply
from previous-answer import *
oMenu = True
while oMenu:
  print("Welcome to the python calculator program.")
  print("""Currently availabe operations:
  a = Addition
  s = Subtraction
  m = Multiplication 
  d = Divison""")
  operation = input("What operation do you want to perform? (a/s/m/d) ").lower()
  numbers = []
  moreNumbers = True
  if operation == "a":
    while moreNumbers:
      numbers.append(float(input("Number: ")))
      yn = input("Do you want to add another number to the calculation? (y/n)").lower()
      if yn == "y":
        moreNumbers = True
        return
      if yn == "n":
        moreNumbers = False
    answer = addition(*numbers)
      
print(answer)
