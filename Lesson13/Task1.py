def count_local_var(func):
    """
    This fucntion takes another function as an argument
    and returns the number of local variables declared
    in that function.
    """
    code = func.__code__
    var_name = code.co.var_name[:code.co_argcount + code.co_nlocals]
    return len([var for var in var_name if var in locals()])


def my_func(a = 1 , b = 2):
    c = a + b
    return c


result = my_func()
print(result)