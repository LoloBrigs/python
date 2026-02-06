from constants import *


class Helicopter:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.water = INITIAL_WATER
        self.water_capacity = INITIAL_WATER_CAPACITY
        self.lives = INITIAL_LIVES

    def move(self, dx, dy, game_map):
        new_x = self.x + dx
        new_y = self.y + dy

        if game_map.is_valid_cell(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True
        return False

    def take_water(self, game_map):
        if game_map.get_cell(self.x, self.y) == CELL_RIVER:
            self.water = self.water_capacity
            return True
        return False

    def extinguish_fire(self, game_map):
        if self.water > 0:
            cell = game_map.get_cell(self.x, self.y)
            if cell == CELL_FIRE:
                game_map.set_cell(self.x, self.y, CELL_TREE)
                self.water -= 1
                return True
        return False

    def visit_hospital(self):
        if self.lives < INITIAL_LIVES:
            self.lives += 1
            return True
        return False

    def upgrade_capacity(self):
        self.water_capacity += 1
        return True

    def take_damage(self):
        self.lives -= 1
        return self.lives > 0

    def get_state(self):
        return {
            'x': self.x,
            'y': self.y,
            'water': self.water,
            'water_capacity': self.water_capacity,
            'lives': self.lives
        }

    def load_state(self, state):
        self.x = state['x']
        self.y = state['y']
        self.water = state['water']
        self.water_capacity = state['water_capacity']
        self.lives = state['lives']
