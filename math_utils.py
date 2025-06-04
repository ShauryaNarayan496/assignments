# this code is defining a module with three functions to calculate the square, cube and check if a number is even 
def square(num):
    return num * num

def cube(num):
    return num * num * num

def number_is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False   
    