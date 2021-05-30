from abc import abstractmethod, ABC


class OfficeEquipment(ABC):
    def __init__(self, name):
        self.name = name
        self.wh = None
        self.dp = None

    def in_warehouse(self):
        return True if self.wh is not None else False

    def _assign_warehouse(self, wh):
        self.wh = wh

    def _assign_department(self, department: str):
        self.dp = department

    @abstractmethod
    def work(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__("Printer")

    def work(self):
        print("Print...")


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__("Scanner")

    def work(self):
        print("Scan...")


class Xerox(OfficeEquipment):
    def __init__(self):
        super().__init__("Xerox")

    def work(self):
        print('Photocopying')


class Warehouse:
    def __init__(self, name):
        self.name = name
        self._equips = {}

    def store(self, equipment):
        equipment.wh = self
        if equipment.name in self._equips:
            self._equips[equipment.name].append(equipment)
        else:
            self._equips[equipment.name] = [equipment]

    def relocate(self, equip_type, department, count):
        if equip_type in self._equips:
            return None

        eq = self._equips[equip_type]
        if len(eq) < count:
            return None

        res = []
        for eq_el in self._equips[equip_type][:count]:
            eq_el.dp = department
            res.append(eq_el)

        del self._equips1[equip_type][:count]
        return res


def store(wh: Warehouse):
    tp = int()
    ct = int()
    try:
        print("Select type:")
        print("1 - Printer")
        print("2 - Scanner")
        print("3 - Xerox")
        tp = int(input("type: "))
        if not 1 <= tp <= 3:
            print("Out of range!")
            return False

        ct = int(input("Select count: "))
        if not ct > 0:
            print("Out of range!")
            return False

        sample = None
        if tp == 1:
            sample = Printer()
        elif tp == 2:
            sample = Scanner()
        else:
            sample = Xerox()

        for i in range(ct):
            wh.store(sample)

    except Exception:
        print("Incorrect!")
        return False

    return True


def show(wh: Warehouse):
    for key in wh._equips.keys():
        print(f"{key} - {len(wh._equips[key])}")

    return True

# Стало лень доделывать
def relocate(wh):
    pass

wh = Warehouse("Main")

while True:
    act = int()
    try:
        print("Select action:")
        print("1 - Store")
        print("2 - Relocate")
        print("3 - Show")
        act = int(input("Action: "))

    except Exception:
        print("Incorrect!")
        continue

    if not 1 <= act <= 3:
        print("Out of range!")
        continue

    res_b = True
    if act == 1:
        res_b = store(wh)
    elif act == 3:
        res_b = show(wh)