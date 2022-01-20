def sum_list_1(dataset: list) -> int:
    # Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7
    sum_list_1 = 0
    for n in dataset:
        sum_list_a = 0
        t = n
        while t != 0:
            sum_list_a += t % 10
            t //= 10
        if sum_list_a % 7 == 0:
            sum_list_1 += n
    return sum_list_1


def sum_list_2(dataset: list) -> int:
    # К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, сумма цифр которых делится нацело на 7
    sum_list_2 = 0
    for m in dataset:
        sum_list_b = 0
        s = m+17
        while s !=0:
            sum_list_2 += s % 10
            s = s // 10
        if sum_list_b % 7 == 0:
            sum_list_2 += m +17
    return sum_list_2



my_list = [i ** 3 for i in range(1, 1000, 2)]
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)