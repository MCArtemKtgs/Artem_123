# # Задача 7_1.
#
# month = 15
#
# spring_months = [3, 4, 5]
# summer_months = [6, 7, 8]
# autumn_months = [9, 10, 11]
# winter_months = [12, 1, 2]
#
# if month in spring_months:
#     print("Весна")
# elif month in summer_months:
#     print("Лето")
# elif month in autumn_months:
#     print("Осень")
# elif month in winter_months:
#     print("Зима")
# else:
#     print("⚠ Некорректный номер месяца!")

# Задача 7_2.

is_logged_in = True # пользователь вошел ли систему
has_items_in_cart = True # в корзине присутствуют ли товары
has_shipping_address = False # адрес доставки
has_order = False # заказ не оформлен

if is_logged_in and has_shipping_address and has_items_in_cart:
    print("✔ Все критерии для оформления заказа выполнены. Заказ может быть оформлен.")
    has_order = True # заказ оформлен
else:
    print("⚠ Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию.")
min_purchase_for_discount = 1000 # мин.сумма для скидки
total_purchase = 1200 # текущая сумма для скидки
is_first_order = False # это первый заказ?

if has_order and (is_first_order or total_purchase >= min_purchase_for_discount):
    print("✔ Вы получаете скидку!")

# Задача 7_3.

number = 7

lucky_numbers = [7, 13, 21]

if number in range(1, 101):

elif number in lucky_numbers:
    print("Счастливое число!")
elif number in number:
    print("Число в указанном диапазоне")
else:
    print("Не повезло!")