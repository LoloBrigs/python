import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def pets_list():
    if not pets:
        print("База данных пуста. Нет питомцев.")
        return

    print("\n=== Список всех питомцев ===")
    for pet_id in pets.keys():
        pet_data = pets[pet_id]
        pet_name = list(pet_data.keys())[0]
        pet_info = pet_data[pet_name]

        pet_type = pet_info["Вид питомца"]
        pet_age = pet_info["Возраст питомца"]
        owner_name = pet_info["Имя владельца"]
        age_suffix = get_suffix(pet_age)

        print(f"ID: {pet_id} - Это {pet_type} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}")
    print()


def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    print("\n=== Создание новой записи ===")
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

    print(f"Питомец {pet_name} успешно добавлен с ID: {new_id}")


def read():
    print("\n=== Чтение информации о питомце ===")
    pet_id = int(input("Введите ID питомца: "))

    pet_data = get_pet(pet_id)

    if pet_data is False:
        print(f"Питомец с ID {pet_id} не найден в базе данных.")
        return

    pet_name = list(pet_data.keys())[0]
    pet_info = pet_data[pet_name]

    pet_type = pet_info["Вид питомца"]
    pet_age = pet_info["Возраст питомца"]
    owner_name = pet_info["Имя владельца"]
    age_suffix = get_suffix(pet_age)

    print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}')


def update():
    print("\n=== Обновление информации о питомце ===")
    pet_id = int(input("Введите ID питомца для обновления: "))

    pet_data = get_pet(pet_id)

    if pet_data is False:
        print(f"Питомец с ID {pet_id} не найден в базе данных.")
        return

    old_pet_name = list(pet_data.keys())[0]
    print(f"Текущее имя питомца: {old_pet_name}")

    pet_name = input("Введите новое имя питомца (или нажмите Enter, чтобы оставить текущее): ")
    if not pet_name:
        pet_name = old_pet_name

    pet_type = input("Введите новый вид питомца: ")
    pet_age = int(input("Введите новый возраст питомца: "))
    owner_name = input("Введите новое имя владельца: ")
    
    pets[pet_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

    print(f"Информация о питомце с ID {pet_id} успешно обновлена.")


def delete():
    print("\n=== Удаление записи о питомце ===")
    pet_id = int(input("Введите ID питомца для удаления: "))

    pet_data = get_pet(pet_id)

    if pet_data is False:
        print(f"Питомец с ID {pet_id} не найден в базе данных.")
        return

    pet_name = list(pet_data.keys())[0]
    confirm = input(f"Вы уверены, что хотите удалить питомца {pet_name} (ID: {pet_id})? (да/нет): ")

    if confirm.lower() == "да":
        del pets[pet_id]
        print(f"Питомец {pet_name} (ID: {pet_id}) успешно удален из базы данных.")
    else:
        print("Удаление отменено.")


def main():
    print("=== Добро пожаловать в систему управления ветеринарной клиникой ===")
    print("Доступные команды: create, read, update, delete, list, stop")

    command = ""

    while command != "stop":
        print("\n" + "-" * 50)
        command = input("Введите команду: ").lower().strip()

        if command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        elif command == "stop":
            print("Программа завершена. До свидания!")
        else:
            print("Неизвестная команда. Доступные команды: create, read, update, delete, list, stop")


if __name__ == "__main__":
    main()
