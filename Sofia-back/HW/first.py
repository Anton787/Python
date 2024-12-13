import time

class Box:
    def __init__(self, items):
        self.items = items  # Количество предметов в коробке

    def __add__(self, other):
        if isinstance(other, Box):
            print('Перекладываем предметы...')
            time.sleep(2)
            return Box(self.items + other.items)
        else:
            raise ValueError("Нельзя сложить коробку и рояль")

    def __str__(self):
        return f"Теперь в 1 коробке {self.items} предметов"

box1 = Box(10)
box2 = Box(5) 

box3 = box1 + box2
print(box3)
