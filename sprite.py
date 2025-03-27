import pygame

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo sprite")

#cargar imagen
sprite_img = pygame.image.load("Kratos.png")
#posicion imagen
x,y = 100,100

#bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        #dibujar imagen
        #Rellenar la pantalla con color
        screen.fill((0,0,0))
        screen.blit(sprite_img,(x,y))
        
        #actualizar la pantalla
        pygame.display.flip()
#salir del juego
pygame.quit()