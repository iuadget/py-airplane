class Settings():

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры корабля
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.ship_limit = 3
        # Параметры пули
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 69, 0)
        self.bullet_allowed = 5
        # Параметры облаков
        self.clouds_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменеющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.cloud_speed_factor = 0.5
        self.clouds_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.cloud_speed_factor *= self.speedup_scale
