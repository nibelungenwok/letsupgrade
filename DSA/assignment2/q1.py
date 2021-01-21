"""Question 1
Write a Python program to print even numbers in a list.
Sample:
Input: list1 = [12, 3, 55, 6, 144]
Output: [12, 6, 144]
Input: list2 = [2, 10, 9, 37]
Output: [2, 10]
Ans:
"""
def filter_even_nums(b):
    a = []
    for i in b:
        if i % 2 == 0:
            a.append(i)
    print(a)
  
if __name__ == "__main__":
    for x in [[12, 3, 55, 6, 144],[2, 10, 9, 37] ]:
        filter_even_nums(x)
