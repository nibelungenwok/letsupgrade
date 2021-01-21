"""
Question 1
Write a Python program to add two numbers using class and object.
(Take both numbers as input from the user)
"""
class Number():
       
    def __init__(self):
        self.a = int(input("please input an integer: "))
    
    def get_value(self):
        return self.a
        
if __name__ == "__main__":
    
    num1 = Number()
    num2 = Number()
    print(num1.get_value() + num2.get_value())
    
