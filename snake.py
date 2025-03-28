import pygame
import random

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600
CELL_SIZE = 20 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

#definicion de colores
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

#Reloj para FPS
clock = pygame.time.Clock()
FPS=10

#fuente para la puntiacion
font = pygame.font.SysFont("consolas",24)

#Funcion para dibujar la serpiente
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen,GREEN,(*segment,CELL_SIZE,CELL_SIZE))

#Funcion para la comida
def draw_food(food_pos):
    pygame.draw.rect(screen,RED,(*food_pos,CELL_SIZE,CELL_SIZE)) 

#funcion para el puntaje
def draw_score(score):
    text= font.render(f"Puntos: {score}",True,WHITE)
    screen.blit(text,(10,10))

#estado inicial de la serpiente
snake = [(100,100),(80,100),(60,100)]
direction = (CELL_SIZE,0)

#posicion aleatoria de la comida
food = (
    random.randrange(0,WIDTH,CELL_SIZE),
    random.randrange(0,HEIGHT,CELL_SIZE)
)

score = 0

#bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0,CELL_SIZE):
                direction = (0,-CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0,-CELL_SIZE):
                direction = (0,CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE,0):
                direction = (-CELL_SIZE,0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE,0):
                direction = (CELL_SIZE,0)
    
    #mover la serpiente agregar nueva cabeza
    head = (snake[0][0] + direction[0],snake[0][1]+direction[1])
    snake.insert(0,head)
    
    #verificar si comio
    if head == food:
        score += 100
        food = (
            random.randrange(0,WIDTH,CELL_SIZE),
            random.randrange(0,HEIGHT,CELL_SIZE)
        )
    else:
        snake.pop()
    
    #verificar colision con los bordes 
    if(
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:]
    ):
        running = False
    
    #Rellenar la pantalla con color
    screen.fill(BLACK)
    
    draw_snake(snake)
    draw_food(food)
    draw_score(score)
    
    #actualizar la pantalla
    pygame.display.flip()
    
    #controlar la velocidad
    clock.tick(FPS)
#salir del juego
pygame.quit()