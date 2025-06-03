def calculate_average(list_a):
    sum = 0
    length = len(list_a)
    for each_num in list_a:
        sum = sum + each_num
    average = sum / length
    return average

list_a = [1,2,3,4,5,6,7,8,9]
print(calculate_average(list_a))