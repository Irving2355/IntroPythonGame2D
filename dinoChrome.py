import pygame
import random
import os 

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-rex Chrome")

#definicion de colores
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

#fuente para la puntiacion
font = pygame.font.SysFont("consolas",24)

#cargar sprites del jugador
sprite_folder = "sprites"
player_sprites = []
for filename in sorted(os.listdir(sprite_folder)):
    if filename.endswith(".png"):
        image = pygame.image.load(os.path.join(sprite_folder,filename)).convert_alpha()
        image = pygame.transform.scale(image,(50,50))
        player_sprites.append(image)

#variables de animacion
current_sprite = 0
animation_speed = 0.2

player_rect = pygame.Rect(100,HEIGHT-150,50,50)
ground = pygame.Rect(0,HEIGHT-50,WIDTH,50)
gravity = 0.5
jump_power = -12
player_speed_y = 0
on_ground = True

#obstaculos
obstacle_width = 30
obstacle_height = 50
obstacle_speed = 5
obstacles = []

for i in range(5):
    x = WIDTH + i * 300
    y = HEIGHT -50 - obstacle_height
    obstacles.append(pygame.Rect(x,y,obstacle_width,obstacle_height)) 

#Reloj para FPS
clock = pygame.time.Clock()
FPS=10

score = 0

passed_obstacles = set()

#bucle principal

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and on_ground:
        player_speed_y = jump_power
        on_ground = False
    
    #movimiento vertical
    player_speed_y +=gravity
    player_rect.y += player_speed_y
    
    #colision con el suelo 
    if player_rect.colliderect(ground):
        player_rect.y = ground.top - player_rect.height
        player_speed_y = 0
        on_ground=True
    
    #mover los obtaculos
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed
        
        if obstacle.right < player_rect.left and id(obstacle) not in passed_obstacles:
            passed_obstacles.add(id(obstacle))
            score += 100
        
    if obstacles and obstacles[0].right < 0:
        obstacles.pop(0)
        new_x = obstacles[-1].x + random.randint(250,400)
        new_obstacle = pygame.Rect(new_x,HEIGHT-50 -obstacle_height,obstacle_width,obstacle_height)
        obstacles.append(new_obstacle)
    
    #coliciones con obstaculos 
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            print("Colision")
            running = False
            
    # animacion del jugador
    current_sprite += animation_speed
    if(current_sprite >= len(player_sprites)):
        current_sprite = 0
    sprite_image = player_sprites[int(current_sprite)]
    
    #dibujar animado
    screen.blit(sprite_image,(player_rect.x,player_rect.y))
    
    #dibujar el suelo y obtaculos
    pygame.draw.rect(screen,GREEN,ground)
    for obstacle in obstacles:
        pygame.draw.rect(screen,RED,obstacle)
    
    text = font.render(f"Puntos: {score}",True,BLACK)
    screen.blit(text,(10,10))
    
    #Rellenar la pantalla con color
    
    
    #actualizar la pantalla
    pygame.display.flip()
#salir del juego
pygame.quit()