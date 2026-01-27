chislo = int(input("Введите целое число: "))
if chislo == 0:
    print("нулевое число")
elif chislo % 2 == 0:
    if chislo > 0:
        print("положительное четное число")
    else:
        print("отрицательное четное число")
else:
    print("число не является четным")

