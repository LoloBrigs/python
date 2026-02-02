X = int(input("Введите натуральное число X: "))

count_deliteley = 0

i = 1
while i * i <= X:
    if X % i == 0:
        count_deliteley += 1
        if i * i != X:
            count_deliteley += 1
    i += 1

print(f"Количество натуральных делителей числа {X}: {count_deliteley}")

