N = int(input("Введите количество чисел: "))

massiv = []
for i in range(N):
    chislo = int(input("Введите число: "))
    massiv.append(chislo)

massiv.reverse()

print("Перевернутый массив:")
for elem in massiv:
    print(elem)


