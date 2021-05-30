# Только благодаря гуглу я понял, что требуется в дз)
# Да и задание взято из первой ссылки...

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def extract(cls, date_str):
        day, month, year = [int(s) for s in date_str.split('-')]
        d = cls(day, month, year)
        return d

    @staticmethod
    def validate(date_str):
        try:
            day, month, year = [int(s) for s in date_str.split('-')]
            return 0 < day < 31 and 0 < month < 13

        except:
            False


if Date.validate('15-02-1999'):
    d1 = Date.extract('15-02-1999')
    print(f"{d1.day} - {d1.month} - {d1.year}")
else:
    print("error!")


