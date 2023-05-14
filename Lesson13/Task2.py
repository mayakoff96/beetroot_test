def outer_function():
    print('outer function')

    def inner_function():
        print('inner function')

    return inner_function


my_func = outer_function()
my_func()
