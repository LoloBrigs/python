import random
from constants import *


class GameMap:

    def __init__(self, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT):
        self.width = width
        self.height = height
        self.cells = [[CELL_EMPTY for _ in range(width)] for _ in range(height)]
        self.clouds = []

    def is_valid_cell(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_cell(self, x, y):
        if self.is_valid_cell(x, y):
            return self.cells[y][x]
        return None

    def set_cell(self, x, y, cell_type):
        if self.is_valid_cell(x, y):
            self.cells[y][x] = cell_type

    def generate_river(self):
        if random.random() > 0.5:
            x = random.randint(2, self.width - 3)
            for y in range(self.height):
                self.set_cell(x, y, CELL_RIVER)
                if random.random() > 0.7:
                    self.set_cell(x + 1, y, CELL_RIVER)
        else:
            y = random.randint(2, self.height - 3)
            for x in range(self.width):
                self.set_cell(x, y, CELL_RIVER)
                if random.random() > 0.7:
                    self.set_cell(x, y + 1, CELL_RIVER)

    def generate_trees(self, count):
        placed = 0
        attempts = 0
        max_attempts = count * 10

        while placed < count and attempts < max_attempts:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.get_cell(x, y) == CELL_EMPTY:
                self.set_cell(x, y, CELL_TREE)
                placed += 1

            attempts += 1

    def generate_random_cells(self, cell_type, count):
        placed = 0
        attempts = 0
        max_attempts = count * 10

        while placed < count and attempts < max_attempts:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.get_cell(x, y) == CELL_EMPTY:
                self.set_cell(x, y, cell_type)
                placed += 1

            attempts += 1

    def spawn_fire(self):
        if random.random() < FIRE_SPAWN_CHANCE:
            trees = []
            for y in range(self.height):
                for x in range(self.width):
                    if self.get_cell(x, y) == CELL_TREE:
                        trees.append((x, y))

            if trees:
                x, y = random.choice(trees)
                self.set_cell(x, y, CELL_FIRE)
                return True
        return False

    def spread_fire(self):
        fires = []
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == CELL_FIRE:
                    fires.append((x, y))

        spread_count = 0
        for fx, fy in fires:
            neighbors = [
                (fx - 1, fy), (fx + 1, fy),
                (fx, fy - 1), (fx, fy + 1)
            ]

            for nx, ny in neighbors:
                if self.is_valid_cell(nx, ny):
                    if self.get_cell(nx, ny) == CELL_TREE:
                        if random.random() < FIRE_SPREAD_CHANCE:
                            self.set_cell(nx, ny, CELL_FIRE)
                            spread_count += 1

        return spread_count

    def burn_fires(self):
        burnt_count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == CELL_FIRE:
                    self.set_cell(x, y, CELL_BURNT)
                    burnt_count += 1
        return burnt_count

    def grow_trees(self):
        grown = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == CELL_EMPTY:
                    if random.random() < TREE_SPAWN_CHANCE:
                        self.set_cell(x, y, CELL_TREE)
                        grown += 1
        return grown

    def count_fires(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get_cell(x, y) == CELL_FIRE:
                    count += 1
        return count

    def get_state(self):
        return {
            'width': self.width,
            'height': self.height,
            'cells': [row[:] for row in self.cells],
            'clouds': self.clouds[:]
        }

    def load_state(self, state):
        self.width = state['width']
        self.height = state['height']
        self.cells = [row[:] for row in state['cells']]
        self.clouds = state['clouds'][:]
