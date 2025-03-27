import pygame

#inicilizar pygame
pygame.init()

WIDTH, HEIGHT = 800,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo sprite mover")

#cargar imagen
sprite_img = pygame.image.load("Kratos.png")
#posicion imagen
x,y = 100,100
velocidad = 5

#bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            x -= velocidad
        if keys[pygame.K_RIGHT]:
            x += velocidad
        if keys[pygame.K_UP]:
            y -= velocidad
        if keys[pygame.K_DOWN]:
            y += velocidad
        
        #dibujar imagen
        #Rellenar la pantalla con color
        screen.fill((0,0,0))
        screen.blit(sprite_img,(x,y))
        
        #actualizar la pantalla
        pygame.display.flip()
#salir del juego
pygame.quit()