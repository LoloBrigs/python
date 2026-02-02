def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_list(n):
    fact_n = factorial(n)

    result_list = []
    for i in range(fact_n, 0, -1):
        result_list.append(factorial(i))

    return fact_n, result_list


if __name__ == "__main__":
    n = int(input("Введите натуральное целое число: "))

    fact_n, fact_list = factorial_list(n)

    print(f"Факториал числа {n} = {fact_n}")
    print(f"Список факториалов от {fact_n} до 1:")
    print(fact_list)
