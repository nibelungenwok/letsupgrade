"""
Question 2
Write a Python program to remove all duplicates words from a given sentence
"""
msg = "are you a are double I not you"
seen = {}
words = msg.split(" ")
for w in words:
    if w in seen.keys():
       words.pop(words.index(w))
    else:
        seen[w] = 1
print(" ".join(words))

