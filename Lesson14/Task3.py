def arg_rules(max_lenght: 15, type_, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f'Argument {arg} is not of type {type_.__name__}')
                    return False
                if len(arg) > max_lenght:
                    print(f'Argument {arg} is longer than {max_lenght} characters')
                    return False
                if not all(symbol in arg for symbol in contains):
                    print(f'Argument {arg} does not contain all required symbols: {contains}')
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator


@arg_rules(type_=str,max_lenght=15, contains=['05','@'])
def create_slogan(name:str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


result_1 = create_slogan('johndoe05@gmail.com')
print(result_1)
result_2 = create_slogan('S@SH05')
print(result_2)