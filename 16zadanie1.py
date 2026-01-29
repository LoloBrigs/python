class Касса:

    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, x):
        self.amount += x
        print(f"Касса пополнена на {x}. Текущая сумма: {self.amount}")

    def count_1000(self):
        thousands = self.amount // 1000
        print(f"В кассе {thousands} целых тысяч")
        return thousands

    def take_away(self, x):
        if x > self.amount:
            raise ValueError(f"Недостаточно денег в кассе! Доступно: {self.amount}, запрошено: {x}")

        self.amount -= x
        print(f"Из кассы изъято {x}. Остаток: {self.amount}")


if __name__ == "__main__":
    print("=== Задание №1: Класс Касса ===\n")

    kassa = Касса(5000)
    print(f"Начальная сумма в кассе: {kassa.amount}\n")

    kassa.top_up(3000)
    print()

    kassa.count_1000()
    print()

    kassa.take_away(2500)
    print()

    kassa.count_1000()
    print()

    print("Попытка изъять больше денег, чем есть в кассе:")
    try:
        kassa.take_away(10000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print(f"\nИтоговая сумма в кассе: {kassa.amount}")
