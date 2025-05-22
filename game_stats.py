class GameStats():
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
    def __init__(self, ai_settings):
        self.game_active = True
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
    def __init__(self, ai_settings):
        self.high_score = 0