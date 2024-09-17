import random

# Объяснение класса и как работать база 

class Orange:
    color = 'orange'
    size = 10
    form = 'sphere'
    
    def to_grow(self):
        self.size += 1 # обращение к экземпляру класса, вызывает ошибку при вызове из класса
        return 'Апельсин растёт'
        
    def fall():
        return 'Апельсин упал'
        
# print(Orange.to_grow())

or1 = Orange()
or1.color = 'light-orange'
or1.to_grow()
print(or1.color, or1.size, Orange.size)
print(type(Orange.fall))
print(type(or1.fall))


print(or1.__dict__)

# Практика по базе ВОИН
# Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. 
# В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. 
# После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
class Warrior:
    name = 'faceless warrior'
    health = 100
    damage = 20
    
    def attack(self, a):
        a.health -= self.damage
        print(f'{self.name} атаковал и оставил {a.name} {a.health} хп')
        
w1 = Warrior()
w2 = Warrior()

w1.name = 'Ember'
w2.name = 'Maks'        

while (w1.health != 0) and (w2.health != 0):
    a = random.randint(0,1)
    if a:
        w1.attack(w2)
    else:
        w2.attack(w1)

winner = w1.name if w2.health == 0 else w2.name
print(f'Победил {winner}')