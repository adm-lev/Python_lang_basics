def translate(numbers_eng, word):

    if word.lower() in numbers_eng:
        if word.istitle():
            return numbers_eng[word.lower()].title()
        return numbers_eng[word]
    else:
        return None


nums_eng = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять',
}


print(translate(nums_eng, input('Введите число для перевода: ')))
