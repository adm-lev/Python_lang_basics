def odd_numbers(amount):
    for i in range(1, amount+1, 2):
        yield i


odd_13 = odd_numbers(13)

print(next(odd_13))
print(next(odd_13))
print(next(odd_13))
print(next(odd_13))
print(next(odd_13))
