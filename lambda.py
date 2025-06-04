# this code is sorting a list of tuples based on the second element of the tuples 
a = [(1,4), (3,2), (5,6), (7,8), (9,10)]
result = sorted(a, key = lambda x: x[1]) 
print(result)