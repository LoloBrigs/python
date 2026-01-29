N = int(input("Введите количество чисел (N): "))

count_zeros = 0

for i in range(N):
    chislo = int(input(f"Введите число {i+1}: "))
    if chislo == 0:
        count_zeros += 1

print(f"Количество нулей: {count_zeros}")

