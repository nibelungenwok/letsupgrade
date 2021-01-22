"""
Question 1
Write a Python program to print all Prime numbers in an Interval.
Question 2
Write a Python Program for factorial of a number.
Question 3
Find the sum of n numbers by using the while loop
"""
start = 2
end = 30

primes = []
for i in range(start, end+1):
    isPrime = True
    if i <= 3:
        isPrime = True
        primes.append(i)
        continue
    for j in range(2, int(i/2)):
        if i % j == 0:
            print(f'{i} is not primes')
            isPrime = False
            break
    if isPrime:
        print(f"{i} in prime")
        primes.append(i)   

print(primes)
