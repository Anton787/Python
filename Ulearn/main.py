import requests
import csv
from datetime import datetime
from xml.etree import ElementTree as ET
from time import time

URL = "http://www.cbr.ru/scripts/XML_daily.asp"
CURRENCIES = ["BYR", "USD", "EUR", "KZT", "UAH", "AZN", "KGS", "UZS", "GEL"]
START_DATE = datetime(2003, 1, 1)
END_DATE = datetime(2024, 11, 1)
OUTPUT_FILE = "student_works/currency.csv"

def fetch_exchange_rates(session, date):
    params = {"date_req": date.strftime("%d/%m/%Y")}
    response = session.get(URL, params=params)
    response.raise_for_status()
    return response.text

def parse_exchange_rates(xml_data, currencies):
    rates = {currency: None for currency in currencies}
    root = ET.fromstring(xml_data)

    for valute in root.findall(".//Valute"):
        char_code = valute.find("CharCode").text
        if char_code in currencies:
            value = float(valute.find("Value").text.replace(",", "."))
            nominal = int(valute.find("Nominal").text)
            rates[char_code] = round(value / nominal, 8)
    return rates

def generate_month_starts(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        next_month = current_date.month % 12 + 1
        year = current_date.year + (current_date.month // 12)
        current_date = datetime(year, next_month, 1)

def main():
    start_time = time()
    data = []

    with requests.Session() as session:
        for date in generate_month_starts(START_DATE, END_DATE):
            xml_data = fetch_exchange_rates(session, date)
            rates = parse_exchange_rates(xml_data, CURRENCIES)
            data.append([date.strftime("%Y-%m")] + [rates[currency] for currency in CURRENCIES])

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["date"] + CURRENCIES)
        writer.writerows(data)

    print(f"Итоговый Время выполнения: {time() - start_time:.2f} секунд")

if __name__ == "__main__":
    main()