"""
Question 1
Write a Python program to remove empty List from List.
"""

lst = [[], [2,3], [1,3,4],[]]

for i in lst:
  if i == []:
    ind = lst.index(i)
    lst.pop(ind)
    
print(lst)
