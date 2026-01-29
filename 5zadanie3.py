X = int(input("Введите минимальную сумму инвестиций (X): "))
A = int(input("Введите сумму у Майкла (A): "))
B = int(input("Введите сумму у Ивана (B): "))

mike_mozhet = A >= X
ivan_mozhet = B >= X
vmeste_mogut = (A + B) >= X

if mike_mozhet and ivan_mozhet:
    print(2)
elif mike_mozhet:
    print("Mike")
elif ivan_mozhet:
    print("Ivan")
elif vmeste_mogut:
    print(1)
else:
    print(0)

