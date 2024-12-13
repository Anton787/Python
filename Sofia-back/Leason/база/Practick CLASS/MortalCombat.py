# Создайте классы Player, Enemy, и Skill. У игрока есть здоровье, список умения и имя, игрок может использовать умение (игрок выбирает на выбор), а также проверять состояние (должно быть описано отедльным методом).
# У каждого умения должно быть нащвание и урон, который он наносит (свойства).
# У класса Enemy есть все те же свойства и методы, отличие в том, что вместо списка умений у врага есть только базовая атака.
# Создайте цикл игры, в котором игрок сталкивается с 10 врагами по очереди. Каждый раз игрок может использовать одно из своих умений для атаки противника, а противник в ответ атакует игрока. 
# Игра продолжается, пока игрок или противник не погибнут. Если игрок побеждает одного врага, он переходит к следующему. Если игрок побеждает всех 10 врагов, он выигрывает.


class Player:
    def __init__(self, name='Мгла', health = 100):
        self.name = name
        self.health = health
    
    def dead(self):
        print(f'Славный был герой {self.name}, но слабый')
    
    def cheack_hp(self):
        print(f'У тебя {self.health}')
    
class Skill:
    def __init__(self, name_one = 'Slip dart', damadge_one = 1, name_two = 'SUPER DAMADGE', damadge_two = 10, name_third = 'MEGA DAMADGE', damadge_third = 100, name_fourth = 'SUPER MEGA DAMAAAAADGE', damadge_fourth = 1000):
        self.name_one = name_one
        self.damadge_one = damadge_one
        self.name_two = name_two
        self.damadge_two = damadge_two
        self.name_third = name_third
        self.damadge_third = damadge_third
        self.name_fourth = name_fourth
        self.damadge_fourth = damadge_fourth
    
    def attack(self, enemy, skill):
        match skill:
            case 1:
                enemy.health -= self.damadge_one
            case 2:
                enemy.health -= self.damadge_two
            case 3:
                enemy.health -= self.damadge_third
            case 4:
                enemy.health -= self.damadge_fourth
        if enemy.health <= 0:
            return 0
        else:
            return 1

class Enemy:
    def __init__(self, name='Tolya', health=1, damage=0):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        player.health -= self.damage
        print(f'{self.name} Нанес {self.damage} урона\n')
        if player.health <= 0:
            player.dead()

    def __del__(self):
        print(f'\n{self.name} просто хотел дружить, а его убил... \n')

all_enemy = {}

quastion = input('Хотите создать героя? Yes-[y] No-[n]')

if quastion == 'y':
    hero_name = input('Введите имя: ')
    hero_health = int(input('Введите количество здоровья: '))
    hero = Player(name=hero_name, health=hero_health)
else:
    hero = Player()

hero_skill = Skill()

i = 1
all_enemy = {}

while len(all_enemy) < 10:
    Enemy_name = input('Введите имя врага: ')
    all_enemy[i] = Enemy(name=Enemy_name, health=i * 5, damage=i + 5)
    i += 1

print('Игра началась, хорошим вам голодных игр!')

i = 1
len = len(all_enemy)
while len > 0 and hero.health >= 0:
    print(f'        Битва {i} \nПротивник {all_enemy[i].name}:  ХП: {all_enemy[i].health} урон:{all_enemy[i].damage}')
    a = int(input(f"Выберите скилл (Ввести номер умения): \n"
            f"1) {hero_skill.name_one}: {hero_skill.damadge_one}\n"
            f"2) {hero_skill.name_two}: {hero_skill.damadge_two}\n"
            f"3) {hero_skill.name_third}: {hero_skill.damadge_third}\n"
            f"4) {hero_skill.name_fourth}: {hero_skill.damadge_fourth} \n\n"))

    if (hero_skill.attack(all_enemy[i], a)):
        all_enemy[i].attack(hero)
    else:
        del all_enemy[i]
        i += 1
        len -= 1
        if len == 0:
            print('Молодец, ты убил всех кто просто хотел подружиться')

input('Конец игры!')



## Вопрос: Почему не работает __del__ у Enemy. Битва идёт, all_enemy уменьшается, return работает, а __del__ не принтит 