import sys
from time import sleep

import pygame
from bullet import Bullet
from cloud import Cloud

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагируем на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Выускаем пулю"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Реагируем на отпускания клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def check_events(ai_settings, screen, ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, ship, clouds, bullets,
                  play_button):

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    clouds.draw(screen)

    # Кнопка отображается в том случае, если игра неактивна
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего отрисованного экрана
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, clouds, bullets):
    """Обновляем позицию пуль"""
    bullets.update()

    # Удаление пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Проверка попадания пуль
    check_bullet_cloud_collision(ai_settings, screen, ship, clouds, bullets)

def check_bullet_cloud_collision(ai_settings, screen, ship, clouds, bullets):
    """Обработка колизий пуль с облаками"""
    collisions = pygame.sprite.groupcollide(bullets, clouds, True, True)

    if len(clouds) == 0:
        # Уничтожение существующих пуль и создание новых облаков
        bullets.empty()
        create_clouds(ai_settings, screen, ship, clouds)


def get_number_clouds_x(ai_settings, cloud_width):
    """Вычисляет количество облаков"""
    available_space_x = ai_settings.screen_width - 2 * cloud_width
    number_clouds_x = int(available_space_x / (2 * cloud_width))
    return number_clouds_x

def get_number_rows(ai_settings, ship_height, cloud_height):
    """Определяем количество рядов"""
    available_space_y = (ai_settings.screen_height -
                         (3 * cloud_height) - ship_height)
    number_rows = int(available_space_y / (2 * cloud_height))
    return number_rows

def create_cloud(ai_settings, screen, clouds, cloud_number, row_number):
    cloud = Cloud(ai_settings, screen)
    cloud_width = cloud.rect.width
    cloud.x = cloud_width + 2 * cloud_width * cloud_number
    cloud.rect.x = cloud.x
    cloud.rect.y = cloud.rect.height + 2 * cloud.rect.height * row_number
    clouds.add(cloud)

def create_clouds(ai_settings, screen, ship, clouds):
    """Создание облаков"""
    cloud = Cloud(ai_settings, screen)
    number_clouds_x = get_number_clouds_x(ai_settings, cloud.rect.width)
    cloud_width = cloud.rect.width
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  cloud.rect.height)

    # Создание рядов облаков
    for row_number in range(number_rows):
        for cloud_number in range(number_clouds_x):
            create_cloud(ai_settings, screen, clouds, cloud_number,
                         row_number)

def check_clouds_edges(ai_settings, clouds):
    """Реагируем на дстижение облаком края экрана"""
    for cloud in clouds.sprites():
        if cloud.check_edge():
            change_clouds_direction(ai_settings, clouds)
            break

def change_clouds_direction(ai_settings, clouds):
    """Опускает все облака и меняет направление движения"""
    for cloud in clouds.sprites():
        cloud.rect.y += ai_settings.clouds_drop_speed
    ai_settings.clouds_direction *= -1

def update_clouds(ai_settings, stats, screen, ship, clouds,
                  bullets):
    """Обновляет позиции облаков"""
    check_clouds_edges(ai_settings, clouds)
    clouds.update()

    # Проверка коллизии корабля с облаком
    if pygame.sprite.spritecollideany(ship, clouds):
        ship_hit(ai_settings, stats, screen, ship, clouds, bullets)

    # check_clouds_bottom(ai_settings, stats, screen, ship, clouds, bullets)

def ship_hit(ai_settings, stats, screen, ship, clouds, bullets):
    """Обработка столкновения"""
    if stats.ships_left > 0:
        # Уменьшение ship_left
        stats.ships_left -= 1

        # Очистка списка облаков и пуль
        clouds.empty()
        bullets.empty()

        # Создание новых облаков и размещение самолета в центре
        create_clouds(ai_settings, screen, ship, clouds)
        ship.center_ship()

        #  Пауза
        sleep(0.5)

    else:
        stats.game_active = False

def check_clouds_bottom(ai_settings, stats, screen, ship, clouds, bullets):
    """Проверяем добрались облака до нижнего края"""
    screen_rect = screen.get_rect()
    for cloud in clouds.sprite():
        if cloud.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, clouds, bullets)
            break