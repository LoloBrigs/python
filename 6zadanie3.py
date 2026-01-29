A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

chetnyye = []

for chislo in range(A, B + 1):
    if chislo % 2 == 0:
        chetnyye.append(chislo)

print(*chetnyye)

