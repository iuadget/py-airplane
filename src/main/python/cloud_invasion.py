import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button

import game_functions as gf

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Airplane")

    # Создание кнопки
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляра для хранения статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля
    ship = Ship(ai_settings, screen)

    # Создание пули
    bullets = Group()

    # создаем облака
    clouds = Group()
    gf.create_clouds(ai_settings, screen, ship, clouds)

    # Запуск основного цикла программы
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        clouds, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                              clouds, bullets)
            gf.update_clouds(ai_settings, screen, stats, sb, ship, clouds,
                  bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, clouds,
                         bullets, play_button)

run_game()