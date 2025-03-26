import pygame
import random 

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cambia de color")

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#color inicial
color = (255,255,255)

#bucle principal

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color=random_color()
        
        #Rellenar la pantalla con color
        screen.fill(color)
        #actualizar la pantalla
        pygame.display.flip()
#salir del juego
pygame.quit()