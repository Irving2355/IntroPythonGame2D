import pygame

# Inicializacion de Pygame
pygame.init()

# Configuracion de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Posiciones y tamaños
paddle_width, paddle_height = 10, 100
ball_size = 10

# Jugadores
player1 = pygame.Rect(20, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)

# Velocidades
ball_speed = [4, 4]
paddle_speed = 6
ball_active = True

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Colocar la peolota con el espacio 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball_active:
                ball.x = WIDTH // 2 - ball_size // 2
                ball.y = HEIGHT // 2 - ball_size // 2
                ball_speed = [4, 4]
                ball_active = True

    keys = pygame.key.get_pressed()
    # Movimiento jugador 1 (W/S)
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed

    # Movimiento jugador 2 (Flechas)
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    # Movimiento de la pelota
    if ball_active:
        # Se aumenta la velocidad en los ejes x,y para que pueda hacer
        # movimientos diagonales  
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Rebote en los bordes superior e inferior
        # solo se invierte su velocidad para que suba o baje
        # esto en el eje Y
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Colision con las paletas de los jugadores
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed[0] = -ball_speed[0]

        # Si la pelota se va por la izquierda o derecha
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_active = False

    # Dibujar barras de los jugadores
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    if ball_active:
        pygame.draw.ellipse(screen, WHITE, ball)
    else:
        # Mostrar mensaje para mas pelotas
        font = pygame.font.Font(None, 48)
        text = font.render("Presiona ESPACIO para nueva pelota", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
