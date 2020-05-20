from mathFuncs import addition, subtract, multiply, divide
from previousAnswer import *
run = True
while run:
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
      if yn == "n":
        moreNumbers = False
    answer = addition(*numbers)
  elif operation == "s":
    while moreNumbers:
      numbers.append(float(input("Number: ")))
      yn = input("Do you want to add another number to the calculation? (y/n)").lower()
      if yn == "y":
        moreNumbers = True
      if yn == "n":
        moreNumbers = False
    answer = subtract(*numbers)
  elif operation == "m":
    while moreNumbers:
      numbers.append(float(input("Number: ")))
      yn = input("Do you want to add another number to the calculation? (y/n)").lower()
      if yn == "y":
        moreNumbers = True
      if yn == "n":
        moreNumbers = False
    answer = multiply(*numbers)
  elif operation == "d":
    while moreNumbers:
      numbers.append(float(input("Number: ")))
      yn = input("Do you want to add another number to the calculation? (y/n)").lower()
      if yn == "y":
        moreNumbers = True
      if yn == "n":
        moreNumbers = False
    answer = divide(*numbers)
  else:
    print("Invalid option.")
  print("----------------------------")
  print("Your answer is:")
  print(answer)
  print("----------------------------")
  runAgain = input("Do you want to solve another calculation? (y/n) ").lower()
  if runAgain == "y":
    run = True
  elif runAgain == "n":
    run = False
  else:
    print("Invalid option.") 
print("---------------------------------")
print("---------- PROGRAM END ----------")
print("---------------------------------")
exit()
