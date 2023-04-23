def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    else:
        print('Invalid operator')


result_1 = make_operation('+', 7, 7, 2)
print(result_1)
result_2 = make_operation('+', -5, -10, 30 ,30)
print(result_2)

