import random

# Описание задачи:

#  1. Создайте базовый класс Character, представляющий общего персонажа.
#  2. Реализуйте в классе Character следующие атрибуты и методы:
#  • Атрибуты:
#  • name: имя персонажа.
#  • health: уровень здоровья (по умолчанию 100).
#  • attack_power: сила атаки (по умолчанию 10).
#  • Методы:
#  • attack(target): метод, позволяющий атаковать другого персонажа, уменьшая его здоровье на величину attack_power.
#  3. Создайте два подкласса, наследующих от Character:
#  • Warrior: воин с повышенной силой атаки.
#  • Mage: маг с возможностью наносить магический урон.
#  4. В каждом подклассе переопределите метод attack для реализации уникального стиля атаки:
#  • Warrior наносит физический урон.
#  • Mage наносит магический урон.
#  5. Создайте объекты Warrior и Mage с уникальными именами.
#  6. Организуйте поочередные атаки между персонажами в случайном порядке.
#  7. После каждой атаки выводите сообщение о том, кто атаковал, кого атаковали и сколько здоровья осталось у цели.
#  8. Сражение продолжается до тех пор, пока здоровье одного из персонажей не станет равным или меньше нуля.
#  9. По завершении сражения выведите сообщение о победителе.

# Требования:

#  • Используйте инкапсуляцию для защиты атрибутов персонажей.
#  • Реализуйте наследование и полиморфизм при создании подклассов и переопределении методов.
#  • Обеспечьте корректную работу программы при различных начальных параметрах персонажей.

# Пример вывода:
# Warrior атакует Mage. У Mage осталось 90 здоровья.
# Mage атакует Warrior. У Warrior осталось 85 здоровья.
# Warrior атакует Mage. У Mage осталось 80 здоровья.
# ...
# Mage атакует Warrior. У Warrior осталось 0 здоровья.
# Mage одержал победу!


class Character:
  def __init__(self, name = 'Oleg', health = 100, magical_resistance = 0, physical_resistance = 0, attack_power = 100):
    self.name = name
    self.health = health
    self.attack_power = attack_power
    self.magical_resistance = magical_resistance
    self.physical_resistance = physical_resistance

  def attack(self, target):
    target.health -= self.attack_power

class Warrior(Character):
  def __init__(self, name='Warrior', health=100, magical_resistance=0, physical_resistance=0.07, attack_power=10):
    super().__init__(name, health, magical_resistance, physical_resistance, attack_power)
    self.attack_power = attack_power + 20
    
  
  def attack(self, target):
    damadge = self.attack_power - (self.attack_power * target.physical_resistance)
    target.health -= damadge
    print(f'{self.name} нанёс {damadge} урона и оставил {target.name} {target.health} здоровья')


class Mage(Character):
  def __init__(self, name='Mage', health=100, magical_resistance=0.08, physical_resistance=0, attack_power=10):
    super().__init__(name, health, magical_resistance, physical_resistance, attack_power)

  def attack(self, target):
    damadge = self.attack_power * 1.2 - (self.attack_power * target.magical_resistance)
    target.health -= damadge
    print(f'{self.name} нанёс {damadge} урона и оставил {target.name} {target.health} здоровья')

class WarriorMage(Character):
  def __init__(self, name='WMage', health=100, magical_resistance=0.04, physical_resistance=0.05, attack_power=10):
    super().__init__(name, health, magical_resistance, physical_resistance, attack_power)

  def attack(self, target):
    a = random.randint(0,1)
    if (a):
      damadge = self.attack_power * 1.1 - (self.attack_power * target.magical_resistance)
    else:
      damadge = self.attack_power * 1.15 - (self.attack_power * target.magical_resistance)
    target.health -= damadge
    print(f'{self.name} нанёс {damadge} урона и оставил {target.name} {target.health} здоровья')

class Fight:
  __classes = {
    '1': Warrior,
    '2': Mage,
    '3': WarriorMage
  }
  def __init__(self):
    one = input('Первый воин')
    two = input('Второй воин')

    self.players = [
        self.__classes[one](),
        self.__classes[two](),
      ]
  def game(self):
    while self.players[0].health > 0 and self.players[1].health > 0:
      a = random.randint(0,1)
      if(a == 1):
        self.players[0].attack(self.players[1])
      else:
        self.players[1].attack(self.players[0])
      if(self.players[0].health < 0):
        print(f'Победил {self.players[1].name} :(')
      elif (self.players[1].health < 0):
        print(f'Победил {self.players[0].name} :(')
        
game = Fight()
game.game()
