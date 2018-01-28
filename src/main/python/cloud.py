import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):
    """Класс представляющий одно облако"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        # Инициализация облако
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения
        self.image = pygame.image.load('images/cloud.png')
        self.rect = self.image.get_rect()

        # Первое появление
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение позиции
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводим облако в текущем положении"""
        self.screen.blit(self.image, self.rect)
