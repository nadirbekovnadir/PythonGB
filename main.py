# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('lesson1')


# ----------------- Первое задание ----------------- #


def first():
    a = 1
    b = 'string'
    c = [1, 'bee', (2, 33)]

    print(c)
    a, b = input('Your name: '), input('Your age: ')
    print()
    print(a, ' ', b)


# first()

# ----------------- Второе задание ----------------- #


def second():
    seconds = int(input('Current time in s: '))
    if seconds < 0:
        print('Error!')
        return

    minutes = seconds // 60

    hours = minutes // 60

    seconds -= minutes * 60
    minutes -= hours * 60

    print(f'Hours: {hours}')
    print(f'Minutes: {minutes}')
    print(f'Seconds: {seconds}')


# second()


# ----------------- Третье задание ----------------- #


def third(k):
    n = int(input('Enter n: '))
    if n > 9:
        print('Error!')
        return

    acc = 0
    res = 0
    for i in range(0, k):
        acc += n
        n *= 10
        res += acc

    print(f'Sum: {res}')


# third(3)


# ---------------- Четвертое задание ---------------- #


def fourth():
    n = int(input('Enter n: '))

    res = 0

    while n != 0:
        digit = n % 10
        n //= 10
        if digit > res:
            res = digit

    print(f'Max: {res}')


# fourth()


# ------------------ Пятое задание ------------------ #


def fifth():
    proceeds = float(input('Proceeds: '))
    costs = float(input('Costs: '))

    if costs >= proceeds:
        print(f'Loss: {costs - proceeds}')
        return

    profit = proceeds - costs
    profitability = profit / proceeds
    print(f'Profitability: {profitability}')

    staff_count = float(input('Number of employees: '))

    per_person = profit / staff_count

    print(f'Profit per employee: {per_person}')


# fifth()


# ------------------ Шестое задание ----------------- #


def sixth():
    a = int(input('a: '))
    b = int(input('b: '))

    rel = b / a
    percent = 0.1

    percent += 1

    res = 1
    while rel > 1:
        rel /= percent
        res += 1

    print(f'Day: {res}')


# sixth()

