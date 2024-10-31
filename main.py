import pygame, sys

#General setup

pygame.init()
clock = pygame.time.Clock()
tick = 60

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Game rectangles

ball = pygame.Rect(screen_width/2 -15,screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width -20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7

player_score = 0
opponent_score = 0

font = pygame.font.Font(None, 74)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Animations

    ball.x += ball_speed_x
    ball.y  += ball_speed_y

    if ball.top  <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.right <= 0 or ball.left >= screen_width:
        ball_speed_x *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1.1

    if player.top <= 0:
        player.top = 0
    
    if opponent.top <= 0:
        opponent.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
    # Teclado

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        opponent.y -= 5
    if keys[pygame.K_s]:
        opponent.y += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    if keys[pygame.K_SPACE]:
        ball_speed_x *= -5


    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    # Renderiza los puntajes
    player_text = font.render(str(player_score), True, (255,255,255))
    opponent_text = font.render(str(opponent_score), True, (255,255,255))
    speed_text = font.render(str(ball_speed_x), True, (255,255,255))
    
    # Posiciona los puntajes
    screen.blit(player_text, (screen.get_width() - 100, 50))  # Puntaje del jugador a la derecha
    screen.blit(opponent_text, (50, 50))  # Puntaje del oponente a la izquierda
    #screen.blit(speed_text,(screen_width/2, 10))
 

    if ball.right <= 0:
        player_score += 1
        ball_speed_x = 7
        ball.x = screen_width / 2
    if ball.left >= screen_width:
        opponent_score += 1
        ball_speed_x = -7
        ball.x = screen_width / 2

    #Actualizar la pantalla

    pygame.display.flip()
    clock.tick(tick)