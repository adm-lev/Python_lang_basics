from functools import wraps


def type_logger(arg):
    def outer(func):
        @wraps(func)
        def wrapper(num):
            if arg(num):
               return func(num)
            else:
                raise ValueError('Число отрицательно')
        return wrapper
    return outer


@type_logger(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

#print('начало кода')
print(calc_cube(3))
print(calc_cube(2))
print(calc_cube(4))
