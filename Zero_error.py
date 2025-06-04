# this code is handling the zero division error and the value error 
try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input")
except Exception as e:
    print(f"Error: {e}")