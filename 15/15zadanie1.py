class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    pass


if __name__ == "__main__":
    autobus = Autobus("Renaul Logan", 180, 12)

    print(f"Название автомобиля: {autobus.name}")
    print(f"Скорость: {autobus.max_speed}")
    print(f"Пробег: {autobus.mileage}")
