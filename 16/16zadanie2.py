class Черепашка:

    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Черепашка движется вверх. Новая позиция: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Черепашка движется вниз. Новая позиция: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Черепашка движется влево. Новая позиция: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Черепашка движется вправо. Новая позиция: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Черепашка эволюционировала! Скорость: {self.s}")

    def degrade(self):
        if self.s <= 1:
            raise ValueError(f"Невозможно уменьшить скорость! Текущая скорость: {self.s}")

        self.s -= 1
        print(f"Черепашка деградировала. Скорость: {self.s}")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves_x = dx // self.s + (1 if dx % self.s != 0 else 0)
        moves_y = dy // self.s + (1 if dy % self.s != 0 else 0)

        total_moves = moves_x + moves_y

        print(f"От позиции ({self.x}, {self.y}) до ({x2}, {y2}) при скорости {self.s}:")
        print(f"  - Расстояние по X: {dx}, ходов: {moves_x}")
        print(f"  - Расстояние по Y: {dy}, ходов: {moves_y}")
        print(f"  - Минимальное количество ходов: {total_moves}")

        return total_moves


if __name__ == "__main__":
    print("=== Задание №2: Класс Черепашка ===\n")

    turtle = Черепашка(0, 0, 1)
    print(f"Начальная позиция: ({turtle.x}, {turtle.y}), скорость: {turtle.s}\n")

    turtle.go_right()
    turtle.go_right()
    turtle.go_up()
    print()

    turtle.evolve()
    print()

    turtle.go_right()
    turtle.go_up()
    print()

    turtle.count_moves(10, 10)
    print()

    turtle.degrade()
    print()

    print("Попытка деградации при минимальной скорости:")
    try:
        turtle.degrade()
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()
