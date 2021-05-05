# ----------------- Первое задание ----------------- #


from sys import argv


def first():
    hours = int(argv[1])
    salary = int(argv[2])
    prize = int(argv[3])

    def zp(hours, salary, prize):
        return hours * salary + prize

    print(f"Заработная плата: {zp(hours, salary, prize)}")


# first()


# ----------------- Второе задание ----------------- #


def second():
    initial = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [initial[i] for i in range(1, len(initial)) if initial[i] > initial[i - 1]]

    print(result)

# second()


# ----------------- Третье задание ----------------- #


def third():
    print([k for k in range(20, 240 + 1) if k % 21 == 0 or k % 20 == 0])


# third()


# ---------------- Четвертое задание ---------------- #


def fourth():
    initial = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    print([k for k in initial if initial.count(k) == 1])


# fourth()


# ------------------ Пятое задание ------------------ #

from functools import reduce


def fifth():
    lt = [k for k in range(100, 1000 + 1, 2)]
    print(lt)

    def multiplication(pr_el, el):
        return pr_el * el

    print(reduce(multiplication, lt))


# fifth()


# ----------------- Шестое задание ----------------- #

from itertools import count, cycle


def sixth():
    def sixth_a(ft: int, lt: int):
        for i in count(ft):
            if i == lt:
                break
            yield i

    def sixth_a_2(ft: int, lt: int):
        iterator = count(ft)
        result = []
        lt = lt - ft
        while lt > 0:
            lt -= 1
            result.append(next(iterator))

        return result

    def sixth_b(iter_list, circles: int):
        counter = 0
        length = len(iter_list)
        # Можно было и while использовать...
        for i in cycle(iter_list):
            yield i

            counter += 1
            if counter == length:
                counter = 0
                circles -= 1

            if circles == 0:
                break

    def sixth_b_2(iter_list, circles: int):
        iterator = cycle(iter_list)
        result = []

        counter = 0
        length = len(iter_list)
        while circles > 0:
            result.append(next(iterator))

            counter += 1
            if counter == length:
                counter = 0
                circles -= 1

            if circles == 0:
                break

        return result

    print("First method:")
    print(f"a: {[k for k in sixth_a(3, 10)]}")
    print(f"b: {[k for k in sixth_b([1, 3, 4, 2], 3)]}")

    print()

    print("Second method:")
    print(f"a: {sixth_a_2(3, 10)}")
    print(f"b: {sixth_b_2([1, 3, 4, 2], 3)}")


# sixth()


# ---------------- Седьмое задание ----------------- #


def seventh():
    def fact(n: int):
        res = 1
        for i in range(0, n):
            res *= i + 1
            yield res

    print(f"Factorial: {[k for k in fact(10)]}")


# seventh()
