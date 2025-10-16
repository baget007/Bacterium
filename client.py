import math
import socket
import time
import pygame


pygame.init()
WIDTH = 800
HEIGHT = 600
CC = WIDTH//2, HEIGHT//2
radius = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бактерии")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настраиваем сокет
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключаем пакетирование
sock.connect(("localhost", 10000))  # IP и порт привязываем к порту

old = [0, 0]
run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            vector = pos[0] - CC[0], pos[1] - CC[1]
            lenv = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            if lenv <= radius:
                vector = 0, 0
            if vector != old:
                old = vector
                sock.send(f"<{vector[0]},{vector[1]}>".encode())
    screen.fill("gray")
    pygame.draw.circle(screen, "red", CC, radius)
    pygame.display.update()

pygame.quit()
