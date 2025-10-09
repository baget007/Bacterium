import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настраиваем сокет
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключаем пакетирование
sock.connect(("localhost", 10000))  # IP и порт привязываем к порту
while True:
    time.sleep(1)
    sock.send("Бобер".encode())