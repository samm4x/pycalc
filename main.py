from mathFuncs import addition, subtract, multiply, divide
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
  try:
    print("----------------------------")
    print("Your answer is:")
    print(answer)
    print("----------------------------")
  except:
    print("There was an error solving that calculation. Possibly a divide by zero error?")
  runAgain = input("Do you want to solve another calculation? (y/n) ").lower()
  if runAgain == "y":
    run = True
  elif runAgain == "n":
    run = False
  else:
    print("Invalid option.") 
print("---------- PROGRAM END ----------")
exit()
