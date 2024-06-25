# Чтение нажатий на клавиатуру
import keyboard

# Функция приёма ивентов (нажатий) и вывод их
def on_key_press(event):
    print(event.name)   

# Принимаем нажатия и отправляем их в функцию
keyboard.on_press(on_key_press)
keyboard.wait()
