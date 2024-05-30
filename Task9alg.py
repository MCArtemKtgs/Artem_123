# Задача 1

# a, s, p = 1, 150, 200
# while True:
#     if a > 10:
#         break
#     a += 2
#     p += a
#     s += p
# print(f'Переменная S={s}')

# a, s, p = 1, 150, 200
# while a <= 10:
#     a += 2
#     p += a
#     s += p
# print(f'Переменная S={s}')

# Задача 2

# s = 1
# for n in range(1, 6):
#     s *= n
# print('Конец алгоритма!')
# print(f'Переменная S = {s}')

# Задача 3

# m, n = 12, 5
# while True:
#     if m == n:
#         break
#     elif m > n:
#         m -= 2*n
#     else:
#         n = n-3
# print(f'Значение переменных m = {m} и n = {n}')

# m, n = 12, 5
# while m != n:
#     if m > n:
#         m -= 2*n
#     else:
#         n = n-3
# print(f'Значение переменных m = {m} и n = {n}')

# Задача 4

# k = []
# l = []
# for i in range(1, 11):
#     k.append(10 - i)
# for i in range(1, 11):
#     l.append(k[5] - k[i - 1])
# print(k)
# print(l)

# k, l = list(range(1, 11)), list(range(1, 11))
# for i in range(1, 11):
#     k[i - 1] = 10 - i
# for i in range(1, 11):
#     l[i - 1] = k[5] - k[i - 1]
# print(k)
# print(l)
# print(f'Количество отрицательных элементов массивы l = {len([value for value in l if value < 0])}')

k, l = list(range(1, 11)), list(range(1, 11))
for i in range(1, 11):
    k[i - 1] = 10 - i
for i in range(1, 11):
    l[i - 1] = k[5] - k[i - 1]
print(k)
print(l)
count_k = 0
for value in k:
    if value < 0:
        count_k += 1
count_l = 0
for value in l:
    if value < 0:
        count_l += 1
print(f'Количество отрицательных элементов = {count_k + count_l}')