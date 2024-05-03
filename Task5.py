# Задача 1. Первый и последний участник.

print("")
print(" > Задача 1")
print("")

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
last_player = list_players[-1]

reestr = {"Первый участник": list_players[0]}

print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

# Задача 1.1. Первый и последний лыжник

print("")
print(" > Задача 1.1")
print("")

list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
last_participants = list_participants[-1]

winner = {"Первый лыжник": list_participants[0]}

print("Последний спортсмен:", last_participants)
print("Первый спортсмен:", winner["Первый лыжник"])

print("")

# Задача 2. Инвентаризация в библиотеке

print(" > Задача 2")
print("")

spk_books = ["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон", "Ревизор", "Гранатовый браслет"]
last_book = (spk_books[-1])

book = {"Пушкин": spk_books[0]}

print("Последняя книга:", last_book)
print("Первая книга:", book["Пушкин"])

# Задача 3. Покупки в интернет-магазине

print(" > Задача 3")
print("")

shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник", "Рюкзак", "Термос", "Миска", "Ветровка", "Коврик"]

unique_items = set(shopping_list)
print("Количество уникальных товаров:", len(unique_items))

# Задача 4. Словарь времен года

print(" > Задача 4")
print("")

seasons_dict = {
    1: "Зима",
    2: "Весна",
    3: "Лето",
    4: "Осень"
}

print("Времена года:", seasons_dict)

# Задача 5. Статистика посещений сайта

print(" > Задача 5")
print("")

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

unique_users = set(users)
print({"Общее количество": len(users), "Уникальные посещения": len(unique_users)})