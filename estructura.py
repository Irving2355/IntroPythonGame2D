import pygame

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi primer juego")

#bucle principal

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
    #Rellenar la pantalla con color
    screen.fill((0,0,0))
    
    #actualizar la pantalla
    pygame.display.flip()
#salir del juego
pygame.quit()