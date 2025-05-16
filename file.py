"""
Скрипт для вычисления среднего значения спектральных данных.
Реализация без использования встроенных функций Python (кроме float()).

Результат: среднее значение величин из файла.

Ссылка на репозиторий с кодом:
https://github.com/anon-spectral-mean/spectral-mean-calculator
"""

import urllib.request

def calculate_mean_from_url(url):
    # Скачиваем файл по ссылке
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    
    # Разбираем данные
    numbers = []
    current_number = []
    for char in data:
        if char in ' \n\t':
            if current_number:
                try:
                    # Пробуем преобразовать собранные символы в число
                    num_str = ''.join(current_number)
                    number = float(num_str)
                    numbers.append(number)
                except ValueError:
                    pass
                current_number = []
        else:
            current_number.append(char)
    
    # Обрабатываем последнее число, если файл не заканчивается пробелом/переносом
    if current_number:
        try:
            num_str = ''.join(current_number)
            number = float(num_str)
            numbers.append(number)
        except ValueError:
            pass
    
    # Вычисляем среднее значение
    total = 0.0
    count = 0
    for num in numbers:
        total += num
        count += 1
    
    if count == 0:
        return 0.0  # чтобы избежать деления на ноль
    
    mean = total / count
    return mean

# URL файла с данными
data_url = "https://cloud.physics.itmo.ru/s/pY68e5CrdtQHF6M"

# Вычисляем среднее значение
mean_value = calculate_mean_from_url(data_url)
print(f"Среднее значение величины: {mean_value}")
