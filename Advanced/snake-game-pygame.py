# A lógica deste jogo não foi executada por mim, estou a usar um tutorial apenas para estudar e fixar os diversos comandos
# O código estará sujo (cheio de comentários) visto ser para meu estudo e eventual pesquisa para relembrar
# Tuplas - espécie de lista imutável que pode conter listas que por sua vez são mutáveis
# 25/01/2022


from tkinter import LEFT, RIGHT
from turtle import down
import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255)) # branco

apple_pos = (random.randint(0, 590), random.randint(0, 590)) # 590 ultima posição sem sair da tela 600 com cada quadrado de 10
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0)) # vermelho

my_direction = LEFT

clock = pygame.time.Clock() # Ajuda a limitar os fps (velocidade)

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Evento do Teclado
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT



    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)    
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    screen.fill((0, 0, 0)) # antes de plotar, precisamos sempre limpar a tela
    screen.blit(apple, apple_pos)
   
    for pos in snake:
        screen.blit(snake_skin, pos) # para plotar precisamos de uma superfície/splite (usamos tupla), posição

    pygame.display.update()
