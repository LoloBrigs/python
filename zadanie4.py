chislo = input("Введите пятизначное целое число: ")

desyatki_tysyach = int(chislo[0])
tysyachi = int(chislo[1])
sotni = int(chislo[2])
desyatki = int(chislo[3])
edinitsy = int(chislo[4])

rezultat = (desyatki ** edinitsy) * sotni / (desyatki_tysyach - tysyachi)

print(f"\nАнализ числа {chislo}:")
print(f"Десятки тысяч: {desyatki_tysyach}")
print(f"Тысячи: {tysyachi}")
print(f"Сотни: {sotni}")
print(f"Десятки: {desyatki}")
print(f"Единицы: {edinitsy}")
print(f"\nФормула: ({desyatki} ^ {edinitsy}) * {sotni} / ({desyatki_tysyach} - {tysyachi})")
print(f"Результат: {rezultat}")
