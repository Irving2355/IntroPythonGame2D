import pygame
import random

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recoje objetos")

#cargar imagen
player_img = pygame.image.load("Kratos.png")
object_img = pygame.image.load("Orbe.png")
player_img = pygame.transform.scale(player_img,(50,50))
object_img = pygame.transform.scale(object_img,(30,30))

#tamanos
player_width,player_height = player_img.get_size()
object_width,object_height = object_img.get_size()

#cargar la musica
pygame.mixer.init()
pygame.mixer.music.load("Song.mp3")
pygame.mixer.music.play(-1)

#posicion iniciales
player_x,player_y = 100,100
object_x,object_y = random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
velocidad = 20
score = 0

#fuente 
font = pygame.font.Font(None,36)

#bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and player_x>0:
            player_x -= velocidad
        if keys[pygame.K_RIGHT] and player_x < WIDTH-player_width:
            player_x += velocidad
        if keys[pygame.K_UP] and player_y>0:
            player_y -= velocidad
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
            player_y += velocidad
        
        #Detectar colisiones
        player_rect = pygame.Rect(player_x,player_y,player_width,player_height)
        object_rect = pygame.Rect(object_x,object_y,object_width,object_height)
        
        if player_rect.colliderect(object_rect):
            score +=1
            object_x = random.randint(50,WIDTH-50)
            object_y = random.randint(50,HEIGHT-50)
        
        #dibujar imagen
        #Rellenar la pantalla con color
        screen.fill((0,0,0))
        screen.blit(player_img,(player_x,player_y))
        screen.blit(object_img,(object_x,object_y))
        
        #mostrar puntuacion
        text = font.render(f"Puntuacion: {score}",True,(255,255,255))
        screen.blit(text,(10,10))
        
        #actualizar la pantalla
        pygame.display.flip()
#salir del juego
pygame.quit()