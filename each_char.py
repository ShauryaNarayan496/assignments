def count_characters(str):
    #create a dictionary to store the count of each character
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

str = input()
print(count_characters(str))
