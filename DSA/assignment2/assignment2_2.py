"""
Question 2
Write a program to print the following pattern
1
22
333
4444
55555
"""
if __name__ == "__main__":
    for i in range(1, 6):
        for j in range(i):
            print(i, end="")
        print()
