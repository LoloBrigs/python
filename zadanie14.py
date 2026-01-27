N = int(input("Введите количество чисел: "))
massiv = list(map(int, input("Введите числа через пробел: ").split()))

novyy_massiv = []
for i in range(N):
    if i == 0:
        novyy_massiv.append(massiv[-1])
    else:
        novyy_massiv.append(massiv[i - 1])

print("Измененный массив:")
print(*novyy_massiv)

