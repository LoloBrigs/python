pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

def get_age_word(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"

pet_name_from_dict = list(pets.keys())[0]
pet_info = list(pets.values())[0]

pet_type_info = pet_info["Вид питомца"]
pet_age_info = pet_info["Возраст питомца"]
owner_name_info = pet_info["Имя владельца"]

age_word = get_age_word(pet_age_info)

print(f'Это {pet_type_info} по кличке "{pet_name_from_dict}". Возраст питомца: {pet_age_info} {age_word}. Имя владельца: {owner_name_info}')
