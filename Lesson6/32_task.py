# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list=[-3, 2, 5, 4, 1, 8, 92, 3, -4, 0]
number_min = int(input('Введи минимальное значение диапазона: '))
number_max = int(input('Введи максимальное значение диапазона: '))
for i in range(len(list)):
    if number_min <= list[i] <= number_max:
        print(i)