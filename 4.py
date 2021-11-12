def thesaurus_adv(*names):
    ex_storage = {}
    ex_list = []
    int_list = []
    #  Список составление списка букв фамилий и его сортировка
    for name in names:
        ind = name.find(' ') + 1
        if name[ind] not in ex_list:
            ex_list.append(name[ind])
    ex_list.sort()
    #  Под каждую букву фамилии подбирается список полных имен сотрудников,
    #  затем сортируется и добавляется в свое место внутрь словаря. В конце итерации переменная списка очищается.
    for letter in ex_list:
        for name in names:
            if ' ' + letter in name:
                int_list.append(name)
        int_list.sort()
        for person in int_list:
            ex_storage.setdefault(letter, {})
            ex_storage[letter].setdefault(person[0], [])
            ex_storage[letter][person[0]].append(person)
        int_list.clear()

    return ex_storage


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева", 'Софокл Аристотель'))
