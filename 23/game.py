import os
import time
import json
import random
from constants import *
from game_map import GameMap
from helicopter import Helicopter
from weather import Weather


class Game:

    def __init__(self):
        self.game_map = None
        self.helicopter = None
        self.weather = Weather()
        self.score = INITIAL_SCORE
        self.tick = 0
        self.game_over = False
        self.hospital_pos = None
        self.shop_pos = None

    def initialize_game(self, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT):
        self.game_map = GameMap(width, height)

        num_rivers = random.randint(1, 3)
        for _ in range(num_rivers):
            self.game_map.generate_river()

        num_trees = (width * height) // 4
        self.game_map.generate_trees(num_trees)

        self.hospital_pos = self._place_special_building(CELL_HOSPITAL)

        self.shop_pos = self._place_special_building(CELL_SHOP)

        heli_x, heli_y = width // 2, height // 2
        self.helicopter = Helicopter(heli_x, heli_y)

        self.score = INITIAL_SCORE
        self.tick = 0
        self.game_over = False

    def _place_special_building(self, building_type):
        placed = False
        attempts = 0
        max_attempts = 100

        while not placed and attempts < max_attempts:
            x = random.randint(0, self.game_map.width - 1)
            y = random.randint(0, self.game_map.height - 1)

            if self.game_map.get_cell(x, y) == CELL_EMPTY:
                self.game_map.set_cell(x, y, building_type)
                placed = True
                return (x, y)

            attempts += 1

        return None

    def update(self):
        if self.game_over:
            return

        self.tick += 1

        if self.tick % TICKS_PER_TREE_GROW == 0:
            self.game_map.grow_trees()

        self.game_map.spawn_fire()

        if self.tick % TICKS_PER_FIRE_SPREAD == 0:
            spread = self.game_map.spread_fire()
            self.score += spread * SCORE_FIRE_SPREAD

            burnt = self.game_map.burn_fires()
            self.score += burnt * SCORE_TREE_BURNT

        self.weather.spawn_cloud(self.game_map)
        self.weather.move_clouds(self.game_map)
        self.weather.generate_lightning(self.game_map)

        if self.weather.start_rain():
            pass

        self.weather.update_rain(self.game_map)

        if self.game_map.get_cell(self.helicopter.x, self.helicopter.y) == CELL_FIRE:
            if random.random() < 0.3:
                if not self.helicopter.take_damage():
                    self.game_over = True

    def process_input(self, command):
        if self.game_over:
            return

        command = command.lower().strip()

        if command == 'w' or command == 'ц':
            self.helicopter.move(0, -1, self.game_map)
        elif command == 's' or command == 'ы':
            self.helicopter.move(0, 1, self.game_map)
        elif command == 'a' or command == 'ф':
            self.helicopter.move(-1, 0, self.game_map)
        elif command == 'd' or command == 'в':
            self.helicopter.move(1, 0, self.game_map)

        elif command == 'e' or command == 'у':
            if self.helicopter.take_water(self.game_map):
                pass

            elif self.helicopter.extinguish_fire(self.game_map):
                self.score += SCORE_TREE_SAVED

            elif self.helicopter.x == self.hospital_pos[0] and self.helicopter.y == self.hospital_pos[1]:
                if self.score >= HEAL_COST:
                    if self.helicopter.visit_hospital():
                        self.score -= HEAL_COST

            elif self.helicopter.x == self.shop_pos[0] and self.helicopter.y == self.shop_pos[1]:
                self.show_shop()

    def show_shop(self):
        while True:
            self.clear_screen()
            print("\n" + "="*50)
            print("🏪 МАГАЗИН УЛУЧШЕНИЙ")
            print("="*50)
            print(f"💰 Ваши очки: {self.score}")
            print(f"💧 Текущая вместимость: {self.helicopter.water_capacity}")
            print("\n1. Увеличить вместимость воды (+1) - {0} очков".format(UPGRADE_WATER_CAPACITY_COST))
            print("2. Выйти из магазина")

            choice = input("\nВыберите действие: ").strip()

            if choice == '1':
                if self.score >= UPGRADE_WATER_CAPACITY_COST:
                    self.helicopter.upgrade_capacity()
                    self.score -= UPGRADE_WATER_CAPACITY_COST
                    print("\n✅ Вместимость увеличена!")
                    time.sleep(1)
                else:
                    print("\n❌ Недостаточно очков!")
                    time.sleep(1)
            elif choice == '2':
                break
            else:
                print("\n❌ Неверный выбор!")
                time.sleep(1)

    def render(self):
        self.clear_screen()

        print("="*60)
        print(f"🎮 ПОЖАРНЫЙ ВЕРТОЛЕТ | Тик: {self.tick} | Очки: {self.score}")
        print(f"❤️  Жизни: {self.helicopter.lives} | 💧 Вода: {self.helicopter.water}/{self.helicopter.water_capacity} | 🔥 Пожары: {self.game_map.count_fires()}")

        if self.weather.is_raining:
            print(f"🌧️  Дождь идет! (осталось {self.weather.rain_timer} тиков)")

        print("="*60)

        for y in range(self.game_map.height):
            row = ""
            for x in range(self.game_map.width):
                if x == self.helicopter.x and y == self.helicopter.y:
                    row += HELICOPTER_IMAGE + " "
                else:
                    is_cloud = False
                    for cloud in self.weather.clouds:
                        if cloud['x'] == x and cloud['y'] == y:
                            row += CELL_IMAGES[CELL_CLOUD] + " "
                            is_cloud = True
                            break

                    if not is_cloud:
                        cell_type = self.game_map.get_cell(x, y)
                        row += CELL_IMAGES[cell_type] + " "

            print(row)

        print("\n" + "="*60)
        print("⌨️  Управление: W/A/S/D - движение | E - действие | Q - сохранить | X - выход")
        print("💡 Набирайте воду над 🌊, тушите 🔥, лечитесь в 🏥, покупайте в 🏪")
        print("="*60)

        if self.game_over:
            print("\n" + "🔴"*20)
            print("💀 ИГРА ОКОНЧЕНА! У вас закончились жизни!")
            print(f"🏆 Финальный счет: {self.score}")
            print("🔴"*20)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def save_game(self, filename='savegame.json'):
        save_data = {
            'game_map': self.game_map.get_state(),
            'helicopter': self.helicopter.get_state(),
            'weather': self.weather.get_state(),
            'score': self.score,
            'tick': self.tick,
            'game_over': self.game_over,
            'hospital_pos': self.hospital_pos,
            'shop_pos': self.shop_pos
        }

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    def load_game(self, filename='savegame.json'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                save_data = json.load(f)

            self.game_map = GameMap()
            self.game_map.load_state(save_data['game_map'])

            self.helicopter = Helicopter(0, 0)
            self.helicopter.load_state(save_data['helicopter'])

            self.weather = Weather()
            self.weather.load_state(save_data['weather'])

            self.score = save_data['score']
            self.tick = save_data['tick']
            self.game_over = save_data['game_over']
            self.hospital_pos = tuple(save_data['hospital_pos'])
            self.shop_pos = tuple(save_data['shop_pos'])

            return True
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return False

    def run(self):
        while True:
            self.render()

            if self.game_over:
                input("\nНажмите Enter для выхода...")
                break

            command = input("\n>>> ").strip()

            if command.lower() == 'x' or command.lower() == 'ч':
                print("Выход из игры...")
                break
            elif command.lower() == 'q' or command.lower() == 'й':
                if self.save_game():
                    print("✅ Игра сохранена!")
                    time.sleep(1)
            else:
                self.process_input(command)

            self.update()
