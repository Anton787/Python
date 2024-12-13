class Table:
    def __init__(self, **props):
        self.w = props['w']
        self.h = props['h']
        self.l = props['l']
        if isinstance(self, KitchenTable):
            p = int(input('Мест за столом: '))
            self.places = p
class DeskTable(Table): #ПРОСТОЕ НАСЛЕДОВАНИЕ
    def square(self):
        return self.w * self.l

class ComputerTable(DeskTable): #ПЕРЕОПРЕДЕЛЕНИЕ
    def square(self, monitor=0):
        return self.w * self.l - monitor

class KitchenTable(Table): #РАСШИРЕНИЕ
    # def __init__(self, **props):
    #     super().__init__(self, **props)
    #     self.places = props['places']
    def sit(self):
        self.places -= 1
        return f'Мест за столом осталось: {self.places}'

params = {'w': 100, 'h': 171, 'l': 80}
table = DeskTable(**params)
table2 = ComputerTable(**params)

print(table.square())
print(table2.square(300))

table3 = KitchenTable(**params)
print(table3.sit())