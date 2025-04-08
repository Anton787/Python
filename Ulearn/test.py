def get_input(prompt, validate_func):
    while True:
        value = input(prompt)
        if validate_func(value):
            return value
        else:
            print("Данные некорректны, повторите ввод")

def is_non_empty_string(value):
    return bool(value.strip())

def is_int(value):
    return value.isdigit()

def is_yes_or_no(value):
    return value.lower() in ["да", "нет"]

def get_word_form(number, words):
    if 11 <= number % 100 <= 19:
        return words[2]
    elif number % 10 == 1:
        return words[0]
    elif 2 <= number % 10 <= 4:
        return words[1]
    else:
        return words[2]

name = get_input('Введите название вакансии: ', is_non_empty_string)
description = get_input('Введите описание вакансии: ', is_non_empty_string)
city = get_input('Введите город для вакансии: ', is_non_empty_string)
experience = int(get_input('Введите требуемый опыт работы (лет): ', is_int))

while True:
    min_salary = input('Введите нижнюю границу оклада вакансии: ')
    if is_int(min_salary):
        min_salary = int(min_salary)
        break
    else:
        print("Данные некорректны, повторите ввод")

while True:
    max_salary = input('Введите верхнюю границу оклада вакансии: ')
    if is_int(max_salary):
        max_salary = int(max_salary)
        if min_salary <= max_salary:
            break
        else:
            print("Нижняя граница оклада должна быть не больше верхней границы. Повторите ввод.")
    else:
        print("Данные некорректны, повторите ввод")

free_schedule = input('Нужен свободный график (да / нет): ').lower() == 'да'
premium = input('Является ли данная вакансия премиум-вакансией (да / нет): ').lower() == 'да'

medium = (max_salary + min_salary) // 2
end_number = medium % 1000

ruble = get_word_form(medium, ['рубль', 'рубля', 'рублей'])
year = get_word_form(experience, ['год', 'года', 'лет'])

print(f'{name}')
print(f'Описание: {description}')
print(f'Город: {city}')
print(f'Требуемый опыт работы: {experience} {year}')
print(f'Средний оклад: {medium} {ruble}')
print(f'Свободный график: {"да" if free_schedule else "нет"}')
print(f'Премиум-вакансия: {"да" if premium else "нет"}')