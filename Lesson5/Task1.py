from random import randint

generated_number = randint(0, 10)

user_input = input('Guess the number: ')

if user_input == generated_number:
    print('You win!')
else:
    print('You lose',generated_number)