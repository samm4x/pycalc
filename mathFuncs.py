def addition(num, *nums):
  for n in nums:
    num += n
  return num

def subtract(num, *nums):
  for n in nums:
    num -= n
  return num

def multiply(num, *nums):
  for n in nums:
    num *= n
  return num

def divide(num, *nums):
  for n in nums:
    num /= n
  return num
