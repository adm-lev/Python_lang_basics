import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes_adv(num, repeats):
    joke = []
    if repeats == 'q' or repeats == 'Q':
        print('До свидания!')
        return False
    if repeats == '0':
        if int(num) > min(len(NOUNS), len(ADVERBS), len(ADJECTIVES)):
            print('Введите число побольше!')
            return True
        else:
            random.shuffle(NOUNS)
            random.shuffle(ADVERBS)
            random.shuffle(ADJECTIVES)
            for i in range(int(num)):
                joke.append(f'{NOUNS[i]} {ADVERBS[i]} {ADJECTIVES[i]}')

    else:
        for i in range(int(num)):
            cur_nouns = random.choice(NOUNS)
            cur_adverbs = random.choice(ADVERBS)
            cur_adjectives = random.choice(ADJECTIVES)
            joke.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    print(joke)
    return True


j = True
while j:
    j = get_jokes_adv(input('Введите пожалуйста число шуток: '),
                      input('Введите 1 для неповторяющахся шуток, 0 ля повторяющихся или q для выхода'))
