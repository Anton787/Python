# Создайте классы Player, Enemy, и Skill. У игрока есть здоровье, список умения и имя, игрок может использовать умение (игрок выбирает на выбор), а также проверять состояние (должно быть описано отедльным методом).
# У каждого умения должно быть нащвание и урон, который он наносит (свойства).
# У класса Enemy есть все те же свойства и методы, отличие в том, что вместо списка умений у врага есть только базовая атака.
# Создайте цикл игры, в котором игрок сталкивается с 10 врагами по очереди. Каждый раз игрок может использовать одно из своих умений для атаки противника, а противник в ответ атакует игрока. 
# Игра продолжается, пока игрок или противник не погибнут. Если игрок побеждает одного врага, он переходит к следующему. Если игрок побеждает всех 10 врагов, он выигрывает.


class Player:
    def __init__(self, name='Мгла', health = '100'):
        self.name = name
        self.health = health
    
    def dead(self):
        print(f'Славный был герой {self.name}, но слабый')
    
    def cheack_hp(self):
        print(f'У тебя {self.health}')
    
class Skill:
    def __init__(self, name_one = 'Slip dart', damadge_one = '1', name_two = 'SUPER DAMADGE', damadge_two = '10', name_third = 'MEGA DAMADGE', damadge_third = '100', name_fourth = 'SUPER MEGA DAMAAAAADGE', damadge_fourth = '1000'):
        self.name_one = name_one
        self.damadge_one = damadge_one
        self.name_two = name_two
        self.damadge_two = damadge_two
        self.name_third = name_third
        self.damadge_third = damadge_third
        self.name_fourth = name_fourth
        self.damadge_fourth = damadge_fourth

class Enemy:
    name = 'Tolya'
    health = 1
    damadge = 0
    
    def attack(self, player):
        player.health -= self.damadge
    
    def __del__(self):
        