def type_logger(func):
    def wrapper(num):

        result = f'{func.__name__}({num}: {type(num)})'

        return result

    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


print(calc_cube(2.5))
print(calc_cube(3))
print(calc_cube(7))
