import urllib.request

def calculate_mean_from_url(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    
    numbers = []
    current_number = []
    for char in data:
        if char in ' \n\t':
            if current_number:
                try:
                    num_str = ''.join(current_number)
                    number = float(num_str)
                    numbers.append(number)
                except ValueError:
                    pass
                current_number = []
        else:
            current_number.append(char)
    if current_number:
        try:
            num_str = ''.join(current_number)
            number = float(num_str)
            numbers.append(number)
        except ValueError:
            pass
    
    total = 0.0
    count = 0
    for num in numbers:
        total += num
        count += 1
    
    if count == 0:
        return 0.0 
    
    mean = total / count
    return mean

# URL файла с данными
data_url = "https://cloud.physics.itmo.ru/s/pY68e5CrdtQHF6M"

mean_value = calculate_mean_from_url(data_url)
print(f"Среднее значение величины: {mean_value}")
