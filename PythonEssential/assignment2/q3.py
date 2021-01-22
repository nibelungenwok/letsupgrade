"""
Question 3
Write a Python program to find all occurrences of a character in the given string
"""
string = "abcbcbcbcbccc"

table = {}
for i in string:
    if i in table.keys():
        table[i] += 1
    else:
        table[i] = 1
        
for key, value in table.items():
    time = "time"
    if value > 1:
        time = "times"
    
    print(f"{key} appears {value} {time}")
