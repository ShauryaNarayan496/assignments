# this code is calculating the factorial of a number 
def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)