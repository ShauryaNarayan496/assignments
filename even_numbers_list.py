# this code is creating a list of even numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num % 2 == 0 for num in numbers]
print(even_numbers)