# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. 
# У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random

class Units:
    def __init__(self, **props):
        self.id = props['id']
        self.team = props['team']

class Soldier(Units):
    def __init__(self, **props):
        self.myHero = None
        super().__init__(**props)
        self.id = props['id']
    def MoveToHero(self, hero):
        self.myHero = hero.id
        return f'Солдат номер {self.id} следует за героем номер {self.myHero}'
    
class Hero(Units):
    def __init__(self, **props):
        super().__init__(**props)
        self.lvl = 0
    def lvlUp(self):
        self.lvl += 1
        return f'Текущий уровень героя {self.id} = {self.lvl}'
team1 = []
team2 = []

hero1 = Hero(**{'id': 1, 'team': team1})
hero2 = Hero(**{'id': 2, 'team': team2})

countSolider = int(input('Сколько солдат создать? '))

i = 1

while i <= countSolider:
    a = random.randint(0,1)
    if a:
        params = {'id': i, 'team': team1}
        solider = Soldier(**params)
        team1.append(solider)
    else:
        params = {'id': i, 'team': team2}
        solider = Soldier(**params)
        team2.append(solider)
    i += 1
    
print(f'Размер войска 1 = {len(team1)} \nРазмер войска 2 = {len(team2)} ')
if len(team1) > len(team2):
    print(hero1.lvlUp())
else:
    print(hero2.lvlUp())

print(team1[4].MoveToHero(hero1))