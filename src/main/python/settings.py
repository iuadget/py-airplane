class Settings():

    def __init__(self):
        # Параметры корабля
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.ship_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 69, 0)
        self.bullet_allowed = 5
        # Параметры облаков
        self.cloud_speed_factor = 0.5
        self.clouds_drop_speed = 10
        #
        self.clouds_direction = 1