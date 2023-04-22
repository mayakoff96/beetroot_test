import random

input_word = input('Enter any word here: ')
n = len(input_word)

for i in range(5):
    rand_word = ''.join(random.sample(input_word, n))
    print(rand_word)