class GameStats():
    """Отслеживание статистики"""

    def __init__(self, ai_settings):
        """Инициализация статистики"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Инициализируем статистику по ходу игры"""
        self.ships_left = self.ai_settings.ship_limit

