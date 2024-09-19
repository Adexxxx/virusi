# Получение IP адреса нашего сервера (компьютера)
import socket

def get_static_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # подключаемся к Google DNS
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

IP_ADDRESS = get_static_ip()
print(IP_ADDRESS)
