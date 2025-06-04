import random 
with open("random_numbers.txt", "w") as file:
    for i in range(10):
        file.write(str(random.randint(1, 10)) + "\n")

with open("random_numbers.txt", "r") as file:
    for line in file:
        print(line)
        