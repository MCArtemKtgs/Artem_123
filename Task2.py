# расчет количества книг на дискете

volume = 1.44
pages = 100
lines = 50
chars = 25
bytes_one_chars = 4

total_chars = pages * lines * chars
total_volume = total_chars * bytes_one_chars
disk_size = 1.44 * 1024 * 1024
num_books = disk_size // total_volume

print('1) Количество книг на дискете:', num_books)

# расчет периметра и площади геометрических фигур

import math

radius = 5
side = 5
pi = 3.1415
square_circle = pi * (radius ** 2)
length_circle = 2 * pi * radius
perimeter1 = 4 * side
square = side ^ 2

#print('Периметр и площадь геомет.фигур:', perimeter, 'см и', square_circle, 'см2 (круг) и', square, 'см2 (квадрат)')
print('2) Периметр:', round(perimeter1, 2), 'см и площадь круга:', round(square_circle, 2), 'и площадь квадрата:', round(square, 2))

# формирование строки из повторяющихся чисел

str_numbers = '0' * 20 + '1' * 50 + '2' * 30

print('3)', str_numbers)

# расчет периметра футбольного поля

length = 90
width = 50
perimeter2 = ( length + width ) * 2

print('4) Периметр футбольного поля:', perimeter2, 'см')

# финансовый калькулятор

money = 10000
add = 5000
money += add

print('5) Кол-во средств после выплаты %:', money, 'руб.')
