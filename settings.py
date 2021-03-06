class Settings():
    #Класс для хранения всех настроек игры
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        #Настройки экрана
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 0, 0)
        #Настройки корабля
        self.ship_limit = 3
        #Настройки пули
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (200, 0, 0)
        self.bullets_alowed = 3
        #настройка пришельцев
        self.fleet_drop_speed = 10
        #Темп ускорения игры
        self.speedup_scale = 1.7
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #Настройка счета
        self.alien_points = 50


    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.7
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        