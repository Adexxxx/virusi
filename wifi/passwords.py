# Получение паролей всех сохранённых сетей Wi-Fi
import subprocess
import time

# Создаем запрос в командной строке netsh wlan show profiles, декодируя его по кодировке в самом ядре
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')

# Создаем список названий всех сохранённых сетей
WiFis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]

# Для каждого имени...
for WiFi in WiFis:
  
# Забираем пароль
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', WiFi, 'key=clear']).decode('cp866').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]

# Пытаемся его вывести в командной строке, отсекая все ошибки
    try:
        print(f'Имя сети: {WiFi}, Пароль: {results[0]}')
    except IndexError:
        print(f'Имя сети: {WiFi}, Пароль не найден!')
