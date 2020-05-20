def addition(num1, *nums): 
    for num in nums: 
        answer = num1 + *nums
    return answer

def subtract(num1, num2):
  answer = num1 - num2
  return answer

def multiply(num1, num2):
  answer = num1 * num2
  return answer

def divide(num1, num2):
  answer = num1 / num2
  return answer
