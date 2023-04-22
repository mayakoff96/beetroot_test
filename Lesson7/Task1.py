# Make a program that has some sentence (a string) on input and returns
# a dict containing all unique words as keys and the number of occurrences as values.


user_input = input('Введіть слова: ')
words = user_input.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)