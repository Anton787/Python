# Напишите программу по следующему описанию:
# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …" (вместо троеточия должны выводиться имя и фамилия объекта).
# В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о сотрудниках и увольте самое слабое звено.
# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.

class Person:
    def __init__(self, name = 'Anton', last_name = 'Gagelganc', qualification = '1'):
        self.last_name = last_name
        self.name = name 
        self.qualification = qualification

    def write_info(self):
        print(f'{self.last_name} {self.name} {self.qualification}')
        
    def __del__(self):
        print(f'До свидания, мистер {self.last_name} {self.name}')
    
p1 = Person()
p1.qualification = 'Supper programmer'

p2 = Person(last_name = 'MS', name='Ivan', qualification='gamer')
p3 = Person(last_name = 'Ivanov', name='Ne ivan', qualification='PHP programmer')

p1.write_info()
p2.write_info()
p3.write_info()

del p3

input()