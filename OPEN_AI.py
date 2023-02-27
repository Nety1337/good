import pygame
import random

# инициализация Pygame
pygame.init()

# настройки окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collect the Coins')

# настройки персонажа
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 0.4

# настройки монет
coin_width = 30
coin_height = 30
coin_x = random.randint(0, screen_width - coin_width)
coin_y = -coin_height
coin_speed = 0.2

# настройки шрифта
font = pygame.font.Font(None, 36)
score = 0

# основной игровой цикл
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # движение монет
    coin_y += coin_speed
    if coin_y > screen_height:
        coin_x = random.randint(0, screen_width - coin_width)
        coin_y = -coin_height
        score += 1

    # обнаружение столкновения монеты и персонажа
    if (player_x + player_width >= coin_x and player_x <= coin_x + coin_width) and \
       (player_y + player_height >= coin_y and player_y <= coin_y + coin_height):
        coin_x = random.randint(0, screen_width - coin_width)
        coin_y = -coin_height
        score += 1

    # отрисовка на экране
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 215, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, (0, 0, 255), (coin_x, coin_y, coin_width, coin_height))

    # отображение счета
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

# завершение Pygame
pygame.quit()