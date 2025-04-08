import math
import pandas as pd
import sqlite3
from datetime import datetime

# Загрузка данных
df_currency = pd.read_csv('student_works/currency.csv', index_col='date')
csv_merged = pd.read_csv('student_works/vacancies_dif_currencies.csv')

# Преобразование индекса валютного DataFrame в формат даты
df_currency.index = pd.to_datetime(df_currency.index, format='%Y-%m')

def convert_salary(row, df_currency):
    salary_from = row['salary_from']
    salary_to = row['salary_to']
    currency = row['salary_currency']
    published_at = row['published_at']
    
    # Если оба оклада отсутствуют, пропускаем вакансию
    if math.isnan(salary_from) and math.isnan(salary_to):
        return ''
    
    # Если указан только один из окладов
    if not math.isnan(salary_from) and math.isnan(salary_to):
        salary = salary_from
    elif math.isnan(salary_from) and not math.isnan(salary_to):
        salary = salary_to
    else:
        salary = (salary_from + salary_to) / 2  # Среднее значение
    
    # Если валюта рубли, возвращаем сумму
    if currency == 'RUR':
        return salary
    
    # Определение месяца и года публикации вакансии
    try:
        published_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S%z').date()
    except ValueError:
        return None

    month_year = pd.Timestamp(published_date.replace(day=1))

    # Получение курса валюты
    if currency in df_currency.columns and month_year in df_currency.index:
        rate = df_currency.loc[month_year, currency]
        if pd.notna(rate):
            return salary * rate  # Конвертация в рубли

    return None  # Пропуск, если курс валюты не найден

# Применяем функцию к каждой строке для расчета оклада
csv_merged['salary'] = csv_merged.apply(convert_salary, axis=1, df_currency=df_currency)

# Удаляем вакансии с неопределенными окладами
filtered_vacancies = csv_merged.dropna(subset=['salary'])

# Формируем итоговый DataFrame
final_data = filtered_vacancies[['name', 'salary', 'area_name', 'published_at']].copy()

# Добавляем индекс столбца 'id'
final_data.reset_index(inplace=True)
final_data.rename(columns={'index': 'id'}, inplace=True)

# Сохраняем результат в SQLite
db_path = 'student_works/vacancies.db'
conn = sqlite3.connect(db_path)

final_data.to_sql('vacancies', conn, if_exists='replace', index=False)
conn.close()

print("Данные успешно обработаны и сохранены в базу данных.")
