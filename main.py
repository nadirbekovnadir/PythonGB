import math

# ----------------- Первое задание ----------------- #


def div(f, s):
    if s == 0:
        raise ZeroDivisionError

    return f / s


# print(div(2, 2))


# ----------------- Второе задание ----------------- #


def print_inf(**kwargs):
    pr_str = str()

    for key, val in kwargs.items():
        pr_str += f"{key}: {val}, "

    if len(pr_str) > 2:
        pr_str = pr_str[0: -2]

    return pr_str


# print(print_inf(name="Nadir", surname="Nadirbekov", by=1999, city="Moscow", email="nadirbekovnadir@gmail.com", phone="89876543210"))


# ----------------- Третье задание ----------------- #


def my_func(a, b, c):
    # Просто сделаю так, будто бы параметров может быть больше двух...
    args = [a, b, c]

    # Здесь тоже можно было сделать бы список
    m1 = max(args)
    args.remove(m1)
    m2 = max(args)

    return m1 + m2


# print(my_func(7, 2, 3))


# ---------------- Четвертое задание ---------------- #


def custom_pow(x, y: int):
    # if y >= 0:
    #     raise Exception("Не надо так делать...")

    res = 1.0

    for i in range(0, abs(y)):
        res *= x

    if y < 0:
        res = 1 / res

    return res


# print(custom_pow(5, -2))


# ------------------ Пятое задание ------------------ #


def fifth():
    summa = 0.0

    def summarizer(str_n: str):
        str_n = str_n.split(' ')
        nonlocal summa

        for el in str_n:
            if el == 'q':
                return False

            summa += float(el)

        return True

    is_exit = True
    while is_exit:
        is_exit = summarizer(input("Введите числа: "))
        print(f"Сумма: {summa}")


# fifth()


# ----------------- Шестое задание ----------------- #


# Может, я не так понял задание...
# И надо было выполнить преобразование, используя смещение между заглавными и обычными буквами в их коде
# (преобразовать в код, вычесть дельту, преобразовать обратно)
def int_func(str_w: str):
    str_w = str_w.title()
    return str_w


print(int_func("pff pff"))
