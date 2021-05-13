# ----------------- Первое задание ----------------- #

import time


# Условие очень странно задано, если честно
class TrafficLight:
    # Чтобы не организовывать прямой и обратный проходы, просто сделаю вот так
    # Правда в жизни оно не так работает...
    __states = ("red", "yellow", "green", "yellow")

    def __init__(self):
        self.__color = 0  # Назвал бы state_pos

    # Сликом странно...
    def running(self, color):
        new_pos = 0 if self.__color + 1 == len(self.__states) else self.__color + 1

        if self.__states[new_pos] != color:
            return False

        self.__color = new_pos

        return True

    def current_state(self):
        return self.__states[self.__color]


def first():
    tl = TrafficLight()

    colors = ("yellow", "green", "yellow", "red", "green")
    # Паузы конечно лучше инкапсулировать в самом классе, выдавая их значения на выход running(), при ошибке == -1
    pauses = {"red": 7.0, "yellow": 2.0, "green": 5.0}

    for color in colors:
        print(f"Light: {tl.current_state()}")
        time.sleep(pauses[tl.current_state()])
        if not tl.running(color):
            print("Error!")
            return
    return


# first()


# ----------------- Второе задание ----------------- #


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, density, thickness):
        return self._length * self._width * density * thickness


def second():
    r = Road(5000, 20)
    print(f"Mass: {r.calculate_mass(25, 5):.2f}")


# second()


# ----------------- Третье задание ----------------- #

import functools


class Worker:
    __income_types = ("wage", "bonus")

    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = dict()

    def set_incomes(self, **kwargs):
        for arg in kwargs.items():
            if arg[0] not in Worker.__income_types:
                raise TypeError("Strange income detected!")

            # Остальные проверки опущу
            self._income[arg[0]] = arg[1]


class Position(Worker):
    # def __init__(self, name, surname, position):
    #    super(Position, self).__init__(name, surname, position)  # Хоть родитель один, оставлю

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_total_income(self):
        return functools.reduce(lambda x, y: x + y, self._income.values())


def third():
    p = Position("Nadir", "Nadirbekov", "student")
    p.set_incomes(wage=1, bonus=2)

    print(f"Full name: {p.get_full_name()}")
    print(f"Total income: {p.get_total_income()}")


# third()


# ---------------- Четвертое задание ---------------- #


class Car:
    def __init__(self, color, name, is_police):
        self._speed = 0
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self, speed):
        if speed == 0:
            self.stop()
            return

        self._speed = speed
        print(f"Car rides: {self._speed}")

    def stop(self):
        self._speed = 0
        print("Car stops")

    def turn(self, direction):
        print(f"Car turns {direction}")

    def show_speed(self):
        print(f"Current speed: {self._speed}")


class SportCar(Car):
    def __init__(self, color, name):
        super(SportCar, self).__init__(color, name, False)


# Можно было бы унаследоваться от SportCar, но это не слишком логично
class TownCar(Car):
    def __init__(self, color, name):
        super(TownCar, self).__init__(color, name, False)

    # Аттрибут максимальной скорости был бы кстати
    def show_speed(self):
        if self._speed > 60:
            print("Speed is too high!")

        super(TownCar, self).show_speed()


class WorkCar(Car):
    def __init__(self, color, name):
        super(WorkCar, self).__init__(color, name, False)

    def show_speed(self):
        if self._speed > 40:
            print("Speed is too high!")

        super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super(PoliceCar, self).__init__(color, name, True)


def fourth():
    sc = SportCar("red", "Sport car")
    tc = TownCar("green", "Town car")
    wc = WorkCar("black", "Work car")
    pc = PoliceCar("blue", "Police car")

    cars = [sc, tc, wc, pc]

    for car in cars:
        print(f"Car name: {car.name}")
        print(f"Car color: {car.color}")
        print(f"Car ispPolice: {car._is_police}")
        car.stop()
        car.show_speed()
        car.go(80)
        car.show_speed()
        car.turn("left")
        print()


# fourth()


# ------------------ Пятое задание ------------------ #


class Stationery:
    def __init__(self, title):
        self._title = title

    def set_title(self, title):
        self._title = title

    def draw(self):
        print("Запуск отрисовки")
        print(f"Создаем {self._title} с {self}")


class Pen(Stationery):
    # Можно было бы переопределить __class__
    # Пошел иным путем, переопределив конвертацию в строку
    def __str__(self) -> str:
        return "ручкой"

    def draw(self):
        super(Pen, self).draw()
        print("Какая красота!")


class Pencil(Stationery):
    def __str__(self) -> str:
        return "карандашом"

    def draw(self):
        super(Pencil, self).draw()
        print("Бррр...")


class Handle(Stationery):
    def __str__(self) -> str:
        return "маркером"

    def draw(self):
        super(Handle, self).draw()
        print("Творить прекрасно!")


def fifth():
    pen = Pen("шедевр")
    pencil = Pencil("еще один шедевр")
    handle = Handle("что-то попроще")

    stationaries = [pen, pencil, handle]
    
    for stationary in stationaries:
        stationary.draw()
        print()


fifth()
