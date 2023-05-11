def math_operation():
    while True:
        try:
            a = float(input('Enter first number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a number.')
    while True:
        try:
            b = float(input('Enter second number: '))
            if b == 0:
                print('Error division by zero!')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')

    try:
        result = a ** 2 / b
        return result
    finally:
        print('')


res = math_operation()
print(res)
