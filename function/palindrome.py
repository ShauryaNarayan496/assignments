# this code is checking if a string is a palindrome 
def is_palindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[len(str) - i - 1]:
            return True
        return False
    

str = input()
print(is_palindrome(str))