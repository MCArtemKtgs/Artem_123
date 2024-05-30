# Циклы for и while

# Задача 8.1. Поиск суммы чисел вводимых с клавиатуры

a = 0
while True:
    n = int(input('n'))
    if n == 0:
        break
    if n > 0:
        a += n
print(a)