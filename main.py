# ----------------- Первое задание ----------------- #


def first():
    my_list = ['string', 8, None, [1, 'test']]

    for el in my_list:
        print(type(el))


# first()


# ----------------- Второе задание ----------------- #


def second():
    inp_list = []
    val = int()

    # Можно конечно было принять значений через пробел
    # Выполнить разделение строки на подстроки (split) и уже по данному набору пройтись
    # Ладно, потренируюсь...
    # while True:
    #     val = input()
    #     try:
    #         inp_list.append(int(val))
    #     except ValueError:
    #         break

    val = input('Print numbers:')
    val = val.split(' ')
    for el in val:
        try:
            inp_list.append(int(el))
        except ValueError:
            break

    for i in range(0, len(inp_list) - 1, 2):
        inp_list[i], inp_list[i + 1] = inp_list[i + 1], inp_list[i]

    print(inp_list)


# second()


# ----------------- Третье задание ----------------- #


def third():
    my_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

    month = int(input('Month number: '))
    for key, value in my_dict.items():
        if month in value:
            print(f'Month name: {key}')
            return

    print('Incorrect number!')


# third()


# ---------------- Четвертое задание --------------- #


def fourth():
    words = input()
    words = words.split(' ')

    for pos, word in enumerate(words):
        print(f'{pos}: {word if len(word) <= 10 else word[0: 10]}')


# fourth()


# ------------------ Пятое задание ----------------- #


# Немного модифицированный бинарный поиск (Не совсем поиск, но то, что нужно)
def binary_search(cont, target):
    left = 0
    right = len(cont) - 1

    m = int()

    while left <= right:
        m = (left + right) // 2

        if cont[m] == target:
            break

        if target > cont[m]:
            right = m - 1
        else:
            left = m + 1

    return m


# Вроде бы проверил корректность работы
def fifth():
    my_list = [7, 5, 3, 3, 2]
    val = int()

    while True:
        val = input()
        try:
            val = int(val)
        except ValueError:
            break

        pos = binary_search(my_list, val)

        while pos < len(my_list):
            if val > my_list[pos]:
                break
            pos += 1

        my_list.insert(pos, val)

    print(my_list)


# fifth()


# ----------------- Шестое задание ----------------- #


# Выберу первое представление из примера
def sixth():
    products = []
    dict_template = {'Название': None, 'Цена': None, 'Кол-во': None, 'Ед': None}

    while True:
        if int(input('Continue?: ')) == 0:
            break

        dict_template['Название'] = input('Название: ')
        dict_template['Цена'] = int(input('Цена: '))
        dict_template['Кол-во'] = int(input('Кол-во: '))
        dict_template['Ед'] = input('Ед: ')

        products.append((len(products) + 1, dict_template.copy()))

    print(products)


sixth()
