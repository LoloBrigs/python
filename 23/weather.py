import random
from constants import *


class Weather:

    def __init__(self):
        self.clouds = []
        self.is_raining = False
        self.rain_timer = 0

    def spawn_cloud(self, game_map):
        if random.random() < CLOUD_SPAWN_CHANCE:
            x = random.randint(0, game_map.width - 1)
            y = random.randint(0, game_map.height - 1)
            self.clouds.append({'x': x, 'y': y, 'life': 10})
            return True
        return False

    def move_clouds(self, game_map):
        new_clouds = []
        for cloud in self.clouds:
            cloud['x'] += random.randint(-1, 1)
            cloud['y'] += random.randint(-1, 1)
            cloud['life'] -= 1

            if cloud['life'] > 0:
                if game_map.is_valid_cell(cloud['x'], cloud['y']):
                    new_clouds.append(cloud)

        self.clouds = new_clouds

    def generate_lightning(self, game_map):
        if self.clouds and random.random() < LIGHTNING_CHANCE:
            cloud = random.choice(self.clouds)
            x, y = cloud['x'], cloud['y']

            if game_map.is_valid_cell(x, y):
                if game_map.get_cell(x, y) == CELL_TREE:
                    game_map.set_cell(x, y, CELL_FIRE)
                    return (x, y)
        return None

    def start_rain(self):
        if not self.is_raining and len(self.clouds) >= 3:
            self.is_raining = True
            self.rain_timer = RAIN_DURATION
            return True
        return False

    def update_rain(self, game_map):
        if self.is_raining:
            self.rain_timer -= 1

            extinguished = 0
            for y in range(game_map.height):
                for x in range(game_map.width):
                    if game_map.get_cell(x, y) == CELL_FIRE:
                        if random.random() < 0.3:
                            game_map.set_cell(x, y, CELL_TREE)
                            extinguished += 1

            if self.rain_timer <= 0:
                self.is_raining = False
                self.clouds = []

            return extinguished
        return 0

    def get_state(self):
        return {
            'clouds': self.clouds[:],
            'is_raining': self.is_raining,
            'rain_timer': self.rain_timer
        }

    def load_state(self, state):
        self.clouds = state['clouds'][:]
        self.is_raining = state['is_raining']
        self.rain_timer = state['rain_timer']
