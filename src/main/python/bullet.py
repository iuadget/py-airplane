import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями"""

    def __init__(self, ai_settings, screen, ship):
        """Создает пулю в текущей позиции корабля"""
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top =  ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещаем пулю вверх по экрану"""
        self.y -= self.speed_factor

        self.rect.y = self.y

    def draw_bullet(self):
        """Выводим пулю на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)