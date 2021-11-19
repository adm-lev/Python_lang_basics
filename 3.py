from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '10А', '10Б', '9А'
]


class_gen = ((tutor, klass) for tutor, klass in zip_longest(set(tutors), set(klasses)))

print(next(class_gen))
print(next(class_gen))
print(next(class_gen))
print(next(class_gen))
print(next(class_gen))
print(next(class_gen))
print(next(class_gen))
print(next(class_gen))  # Наступило истощение
