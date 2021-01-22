"""
Question 3
Find the sum of n numbers by using the while loop
"""
arr = [1, 2, 3, 4]
sum = 0
i = 0
while i < len(arr):
  sum += arr[i]
  i += 1
  
print(sum)
