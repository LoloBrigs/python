def print_list_recursive(my_list, index=0):
    if index >= len(my_list):
        print("Конец списка")
        return

    print(my_list[index])

    print_list_recursive(my_list, index + 1)


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    print("=== Задание №1: Рекурсивный вывод списка ===\n")
    print("Исходный список:")
    print(my_list)
    print("\nВывод элементов с помощью рекурсии:")

    print_list_recursive(my_list)
