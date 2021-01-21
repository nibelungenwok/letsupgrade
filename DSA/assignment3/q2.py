"""
Question 2
Define a function swap that should swap two values and print the swapped variables outside the
swap function.
"""
def swap(a, b):
    return b, a

if __name__ == "__main__":
  a = 3
  b = 4
  
  a, b = swap(a, b)
  print(a, b)
