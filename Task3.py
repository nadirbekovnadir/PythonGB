import traceback

class ContainedTypeError(Exception):
    def __init__(self, text):
        self.text = text

    @classmethod
    def check(cls, value):
        try:
            return float(value)

        except:
            raise cls(f"Type error!\n{traceback.format_exc()}")
            return None


l = list()
while True:
    string = input("Enter value:")
    if string == "q":
        break

    try:
        l.append(ContainedTypeError.check(string))
    except ContainedTypeError as err:
        print(err)
    else:
        print(l)

