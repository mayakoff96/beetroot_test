def logger(func):
    def wrapper(*args, **kwargs):
        print(f'{wrapper} called with {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1 ,2 ,3)