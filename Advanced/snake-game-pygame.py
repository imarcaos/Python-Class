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

apple_pos = (random.randint(0, 590), random.randint(0, 590)) # 590 ultima posição sem sair da tela 600
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0)) # vermelho

my_direction = LEFT

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0)) # antes de plotar, precisamos sempre limpar a tela
    screen.blit(apple, apple_pos)
   
    for pos in snake:
        screen.blit(snake_skin, pos) # para plotar precisamos de uma superfície/splite (usamos tupla), posição

    pygame.display.update()
