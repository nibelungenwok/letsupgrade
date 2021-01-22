"""
Question 2
Take two lists as input list1 = [1,2,3,4,5] and list2 = ["a", "b", "c", "d", "e"] From that make a
dictionary ouput {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
"""
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
dict1 = {}
for num in list1:
    for alphabet in list2:
        dict1[num] = alphabet
print(dict1)
