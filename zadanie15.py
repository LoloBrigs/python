m = int(input("Введите максимальную массу лодки: "))
n = int(input("Введите количество рыбаков: "))

vesa = []
for i in range(n):
    ves = int(input("Введите вес рыбака: "))
    vesa.append(ves)

vesa.sort()

lodki = 0
left = 0
right = n - 1

while left <= right:
    if vesa[left] + vesa[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    lodki += 1

print(f"Минимальное количество лодок: {lodki}")

