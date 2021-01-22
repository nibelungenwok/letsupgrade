"""
Question 2
Write a Python Program for factorial of a number.
"""
def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num-1)
