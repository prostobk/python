#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

#n = int(input('Введите число N: '))
#k = 0
#res = 1
#while res < n+1:
#    print(res, end=' ')
#    k += 1
#    res = 2 ** k

list_1 = [1, 2, 3, 4, 5]
k = 4

count = 0
count1 = 0
for i in range(len(list_1)):
    if k == list_1[i]:
        count = i
        count1 = count
    else:
        (k-list_1[i]) < k-count and k-list_1[i] > 0
        count1 = i
print(list_1[count])