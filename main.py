# ----------------- Первое задание ----------------- #


def first():
    cont = []

    # Чем такая конструкция, лучше try catch с finally (просто можно добавить доп. обработку)
    # Но оставлю так)
    with open("first.txt", 'w') as f:
        while True:
            cont.append(input("Enter text: "))
            if cont[-1] == "":
                break
            cont[-1] += '\n'

        f.writelines(cont)


# first()


# ----------------- Второе задание ----------------- #


def second():
    try:
        f = open("second.txt", 'r')
        count = 0
        # Можно было бы и все строки сразу прочитать
        for line in f:
            count += 1
            print(f"Length of {count} line: {len(line)}")

        print(f"Lines count: {count}")
    except IOError:
        print("OOps")
    finally:
        f.close()


# second()


# ----------------- Третье задание ----------------- #


def third():
    try:
        f = open("third.txt", 'r', encoding="utf-8")
        aver = 0.0
        # Конечно лучше было бы простым циклом... (Несмотря на вычислительную неэффективность подхода, поупражняюсь)
        # Не использую регулярные выражения, пройдусь по обычным функциям
        # Можно было бы конечно воспользоваться filter + isdigit
        zps = {line.split(' ')[0]: float(line.strip('к\n').split(' ')[-1]) for line in f}
        # zps = {line.split(' ')[0]: float(''.join(filter(lambda ch: ch.isdigit(), line.split(' ')[-1]))) for line in f}
        # print(zps)
        print(f"Average: {sum(zps.values()) / len(zps) : .2f}")

        for item in filter(lambda item: item[1] <= 20, zps.items()):
            print(f"{item[0]}: {item[1]}")

    except IOError:
        print("OOps")
    finally:
        f.close()


# third()


# ---------------- Четвертое задание ---------------- #


def fourth():
    num_dict = {
        "1": "Один",
        "2": "Два",
        "3": "Три",
        "4": "Четыре",
        "101010": "И т.д."
    }

    try:
        f_inp = open("fourth_input.txt", 'r', encoding="utf-8")
        f_out = open("fourth_output.txt", 'w', encoding="utf-8")

        for line in f_inp:
            line = [ln.strip() for ln in line.split('—')]
            line[0] = num_dict[line[-1]]
            line = ' — '.join(line) + "\n"
            f_out.write(line)

    except IOError:
        print("OOps")
    finally:
        f_inp.close()
        f_out.close()


# fourth()


# ------------------ Пятое задание ------------------ #


def fifth():
    try:
        f = open("fifth.txt", "w+", encoding="utf-8")

        f.write("12 13.4 14.4 sds 123")

        def try_parse(s: str):
            try:
                float(s)
            except ValueError:
                return False

            return True

        last = f.tell()
        f.seek(0)
        nums = [float(nl) for nl in f.read().split(' ') if try_parse(nl)]
        summa = sum(nums)

        f.seek(last)
        f.write("\n" + str(summa))
        print(f"Sum: {summa}")

    except IOError:
        print("OOps")
    finally:
        f.close()


# fifth()


# ----------------- Шестое задание ----------------- #


def sixth():
    with open("sixth.txt", 'r', encoding="utf-8") as f:
        def parse_num(s: str):
            try:
                return float(''.join([c for c in s if c.isdigit() or c == '.']))
            except ValueError:
                return None

        dict_less = dict()

        # В конце концов, если мне была бы нужна производительность, писал бы на плюсах...
        for line in (line.strip().split(':') for line in f):
            line[1] = [parse_num(s) for s in line[1].strip().split(' ') if parse_num(s) is not None]
            dict_less[line[0]] = sum(line[1])

        print(dict_less)


# sixth()


# ---------------- Седьмое задание ----------------- #

import json


def seventh():
    with open("seventh_input.txt", 'r') as f_inp:
        firm_dict = dict()
        for line in f_inp:
            line = line.strip().split(' ')
            firm_dict[line[0]] = float(line[2]) - float(line[3])

        aver_dict = dict([("Average", sum(firm_dict.values()))])
        res = [firm_dict, aver_dict]

        with open("seventh_output.txt", 'w') as f_out:
            json.dump(res, f_out)


seventh()















