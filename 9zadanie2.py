import sys

lines = []
for line in sys.stdin:
    line = line.strip()
    if line:
        lines.append(line)

list1 = set()
list2 = set()

reading_first = True
for line in lines:
    try:
        num = int(line)
        if reading_first:
            list1.add(num)
        else:
            list2.add(num)
    except ValueError:
        reading_first = False
        continue

if not list2:
    all_numbers = list(list1)
    mid = len(all_numbers) // 2
    list1 = set(all_numbers[:mid])
    list2 = set(all_numbers[mid:])

common_count = len(list1 & list2)

print(common_count)
