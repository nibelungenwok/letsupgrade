"""
Question 1
Write a Python program to merge two files into a third file.
"""

path_file1 = input("Please input file1 path:")
path_file2 = input("Please input file2 path:")

with open(path_file1, 'a') as fp1:
    with open(path_file2, 'r') as fp2:
        fp1.writelines(fp2.readlines())
