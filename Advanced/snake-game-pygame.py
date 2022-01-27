# A lógica deste jogo não foi executada por mim, estou a usar um tutorial apenas para estudar e fixar os diversos comandos
# O meu código estará sujo (cheio de comentários) visto ser para meu estudo e eventual pesquisa para relembrar
# Tuplas - espécie de lista imutável que pode conter listas que por sua vez são mutáveis
# 25/01/2022

import pygame, random
from pygame.locals import *

# Função para alinhar as casas decimais da maçã
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10) # Ao fazer esta divisao excluo unidade e deixo as decimais, para ficar alinhado

# Função Teste de colisão
def collision (c1, c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))


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

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0)) # vermelho

my_direction = LEFT

clock = pygame.time.Clock() # Ajuda a limitar os fps (velocidade), inserindo no tick abaixo

game_over = False

while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

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

    # Testa colisão da Snake com a Maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random() # nova posição para a maçã
        snake.append((0, 0)) # adiciona um novo item ao final da lista (+ 1 pedaço da calda)

    
    # Testa Colisão da Cabeça da cobra com seu corpo
    if snake[0] in snake[1:]:
        game_over = True            
        break   
    #for i in range(1, len(snake) - 1):
    #    if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
    #        game_over = True            
    #        break

    if game_over:
        break

    # organiza a posição ocupada pela cobra e restante do corpo
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # direções da Cobra    
    if my_direction == UP:
        # A seguir verifico se a cobra esta no limite do mapa e redireciono para a outra extremidade
        if (snake[0][0], snake[0][1]) > (snake[0][0], 0):
            snake[0] = (snake[0][0], snake[0][1] - 10)
        else:
            snake[0] = (snake[0][0], 600)   
    if my_direction == DOWN:
        if (snake[0][0], snake[0][1]) < (snake[0][0], 600):
            snake[0] = (snake[0][0], snake[0][1] + 10)
        else:
            snake[0] = (snake[0][0], 0)   
    if my_direction == RIGHT:
        if (snake[0][0], snake[0][1]) < (600, snake[0][1]):
            snake[0] = (snake[0][0] + 10, snake[0][1])
        else:
            snake[0] = (0, snake[0][1])
    if my_direction == LEFT:
        if (snake[0][0], snake[0][1]) > (0, snake[0][1]):
            snake[0] = (snake[0][0] - 10, snake[0][1])
        else:
            snake[0] = (600, snake[0][1])
        
    
    screen.fill((0, 0, 0)) # antes de plotar, precisamos sempre limpar a tela
    screen.blit(apple, apple_pos)
   
    for pos in snake:
        screen.blit(snake_skin, pos) # para plotar precisamos de uma superfície (usamos tupla), posição

    pygame.display.update()
