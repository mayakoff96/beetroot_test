def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        print('Invalid operator')


result_1 = make_operation('+', 7, 7, 2)
print(result_1)
result_2 = make_operation('-', 5, 5, -10, -20)
print(result_2)
result_3 = make_operation('*', 7, 6)
print(result_3)