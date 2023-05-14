# Запитуємо від користувача вираз та очікувану відповідь
expression = input("Enter a mathematical expression: ")
expected_answer = eval(expression)

# Запитуємо від користувача його відповідь та перевіряємо, чи вона правильна
user_answer = float(input("What is the answer to the expression? "))
if user_answer == expected_answer:
    print("You are correct!")
else:
    print("Sorry, the correct answer is", expected_answer)