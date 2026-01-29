slovo = input("Введите слово из маленьких латинских букв: ")

glasnye = ['a', 'e', 'i', 'o', 'u']

count_a = slovo.count('a')
count_e = slovo.count('e')
count_i = slovo.count('i')
count_o = slovo.count('o')
count_u = slovo.count('u')

kolichestvo_glasnyh = count_a + count_e + count_i + count_o + count_u

print(f"\nАнализ слова '{slovo}':")
print(f"Гласных букв: {kolichestvo_glasnyh}")

print(f"\nКоличество буквы 'a': {count_a if count_a > 0 else False}")
print(f"Количество буквы 'e': {count_e if count_e > 0 else False}")
print(f"Количество буквы 'i': {count_i if count_i > 0 else False}")
print(f"Количество буквы 'o': {count_o if count_o > 0 else False}")
print(f"Количество буквы 'u': {count_u if count_u > 0 else False}")

