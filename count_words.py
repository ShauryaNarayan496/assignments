def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = "random_numbers.txt"
words_count = count_words(filename)
print("Number of words:", words_count)
