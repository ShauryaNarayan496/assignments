# this code is calculating the sum of even numbers from 1 to 100 
num = int(input()) 
sum = 0 
for each_num in range(1, 101):
    if (each_num % 2 == 0):
        sum = sum + each_num 
print(sum) 

