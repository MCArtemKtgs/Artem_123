# Тема: Базовые объектные типы языка Python - tuple,dict

# create - создать
# retrive (read) - получить, прочитать
# update - изменить
# delete - удалить

# tuple кортеж
a = (1, 1.2, 'hello')
# словарь dict
a = {'a':1, 'b':1.2, 'c': 'hello'}

# Кортеж tuple (Составной тип данных)

# create - создать
a = (1, 1.1, 'a', [4, 5, 6], {'a':1, 'b':2}, None, True)
a = ()
b = tuple()
b = (1,)

a = [1, 2.1, 3] # это список list
tuple(a) # (1, 2.1, 3)
b = tuple('abc') # ('a', 'b', 'c')

# retrive (read) - получить и прочитать

a = (1, 2.1, 'd') # в кортеже можно обращаться к элементу по индексу
a[0] # 1
a[2] # 'd'

# update - изменить
a = (1, 1.1, 'a')
a[0] = 'a' # Ошибка.
a = (1, 2, 3) # Теперь 'a' равно (1, 2, 3)

# delete - удалить

a = (1, 1.1, 'a')
del a[0] # Ошибка.
del a # Полное удаление переменной "a"

# Кортеж tuple (Действия с кортежами)

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c) # (1, 2, 3, 4, 5, 6)
a += b # Теперь "a" равно (1, 2, 3, 1, 2, 3)

# (Действия с объектами)

a = (1, 2, 3) # Это одномерный кортеж
b = ((1, 2, 3), (4, 5, 6), (7, 8, 9)) # Это двумерный (кортеж в кортеже) кортеж. Его можно представить как: ((1, 2, 3), (4, 5, 6), (7, 8, 9))

b[0] # Получение 1-ого кортежа (1, 2, 3)
b[0][0] # Получение 1-ого элемента "1" из 1-ого кортежа (1, 2, 3)
b[-1][-1] # Получение последнего элемента "9" из последнего кортежа (7, 8, 9)

# Методы tuple
# a.count() и a.index()

help(tuple) # Информация о кортежах
a = (1, 2, 1)
a.count(1) # 2. Возвращает сколько раз в кортеже встретилось передаваемое значение. В примере вернётся 2, т.к. в кортеже 2 единицы.
a.index(2) # 1. Возвращает индекс, где передаваемое значение стоит в кортеже. В примере вернётся 1, т.к. значение 2 в кортеже стоит на 1-ом индексе.

# Практические моменты

a = (1, 2, [1, 2, 3])
a[2][0] = 10 # Теперь "a" (1, 2, [10, 2, 3]), т.к. внутри кортежа мы можем обратиться к изменяемому типу, хотя a[1] = 10 нам не позволит сделать.
a = [1, 2, 3] # Создали список
b = (1, 2, a) # Передали "a" в кортеж. "b" = (1, 2, [1, 2, 3]). Но "a" это список, поэтому если изменить значение в "a", то оно автоматом поменяется в "b"
a[1] = 20 # Теперь "a" равно [1, 20, 3].
print(b) # (1, 2, [1, 20, 3]), т.к. "a" это список который внутри кортежа "b".

# Словарь (dict)

# create создать dict

a = {'a':1} # словарь из одного элемента ключ 'a', значение 1

a = {'a':1, 'b': 2} # Словарь из двух элементов (ключ "a", значение 1, ключ "b", значение 2)

a = dict([['a', 1],['b', 2]]) # Это создаст словарь {'a':1, 'b':2}

a = dict(a=1, b=2) # Это создаст словарь {'a':1, 'b':2}

a = {} # Это пустое множество
b = dict() # А это пустой словарь

a = dict([['a', 1], ['b', 2]]) # Передан список списков. Это создаст словарь {'a':1, 'b':2}
a = dict((('a', 1),('b', 2))) # Передан кортеж кортежей. Это создаст словарь {'a':1, 'b':2}

a = {1: 'a', 1.1: 'b', 'c': 3, (1, 2): [1, 2, 3], frozenset({1, 2}): {1, 2}, 4: {1:2, 3:4}, print: 4} # {1:'a', 1.1:'b', 'c':3, (1, 2): [1, 2, 3], frozenset({1, 2}): {1, 2}, 4:{1:2, 3:4}, <built-in function print>: 4}
a = {'a': 1, 'a': 3, 'b': 2} # {'a':3, 'b':2}. При одинаковых ключах - запишется то значение, чтобы объявлено последним!

# retrive (read) получить и прочитать

a = {'a': 1, 'b': 1.1}
print(a) # {'a':1, 'b': 1.1}
print({'a': 1,'b': 1.1}) # {'a':1, 'b': 1.1}

a = {'a': 1, 'b': 1.1, 1: 'abc'}
a[0] # Будет ошибка, т.к. ключа 0 не существует в словаре
a['a'] # 1
a['b'] # 1.1
a[1] # 'abc'
var_b = 'b'
a[var_b] # 1.1. Т.к. значение var_b = 'b'

a = {'a': 1, 'b': 1.1, 1: 'abc'}
a.get('a') # 1
a.get(0) # None. сли ключа не существует, то по умолчанию вернется None.
a.get(0, 'a') # 'a'. Если нет ключа, то вернётся то, что было передано вторым.

# update изменить
a = {'a': 1, 'b': 1.1}
a['c'] = 2 # Добавили в словарь ключ "c" со значением 2. Теперь "a' {'a':1, 'b':1.1, 'c':2}

a = {'a': 1, 'b': 1.1}
a.setdefault('c',2) # Теперь "a" равно {'a':1, 'b':1.1, 'c':2}

a = {'a': 1, 'b': 1.1}
a.update({'a':10, 'c':'abc'}) # Теперь "a" равно {'a':10, 'b':1.1, 'c':'abc'}

a = {'a': 1, 'b': 1.1}
a['b'] = 2 # Теперь "a" {'a':1, 'b':2}

a = {'a': 1, 'b': 1.1}
a.setdefault('b', 2) # setdefault не позволит установить значение 2 по ключу 'b' т.к. там уже есть элемент. "a" равно {'a':1, 'b':1.1}

# delete удалить

# Для удаления элемента из словаря есть методы
# a.clear(), popitem(), pop(key

a = {'a': 1, 'b': 1.1}
del a['a'] # Теперь словарь "a" {'b': 1.1}
del a # Полное удаление словаря "a"

a = {'a': 1, 'b': 1.1}
a.clear() # Очистка словаря теперь "a" {}
a = {'a': 1, 'b': 1.1}
a.popitem() # ('b', 1.1). Возвращает последний элемент (ключ, значение) в словаре и удаляет его. Теперь "a" {'a':1}.

a = {'a': 1, 'b': 1.1}
a.pop('a') # 1. Возвращает значение по переданному ключу и удаляет этот элемент из словаря. Теперь "a" {'b':1.1}.

# Словарь (dict) - Действия с объектами

a = {'a': 1, 'b': 1.1} # Это простой словарь
b = {'a': 1, 'b': {'c': 10}} # Это вложенный словарь (словарь в словаре)

b = {'a': 1, 'b': {'c': 10}}
b['b'] # Получение вложенного словаря {'c': 10}
b['b']['c'] # Получение 10 из {'c': 10}

# Методы

help(dict) # Информация о словарях
a = {'a': 1, 'b': 1.1}
a.copy() # {'a':1, 'b':1.1} Возвращает копию словаря.
a.values() # dict_values([1, 1.1]). Возвращает объект в котором содержатся все значения словаря (без ключей).
a.keys() # dict_keys(['a', 'b']). Возвращает объект в котором содержатся все ключи словаря (без значений).
a.items() # dict_items([('a', 1), ('b', 1.1)]). Возвращает объект в котором содержатся пары (ключ, значение).
dict.fromkeys(['a', 'b', 'c'], 10) # {'a':10, 'b':10, 'c':10}. Специальный метод возвращающий словарь созданный на основе списка ключей (keys) и заполненных одинаковыми данными из value.

# Практические моменты

products = {
    'апельсин': {'цена': 100, 'вес': 0.5},
    'банан': {'цена': 110, 'вес': 1},
} # Словарь с продуктами
products['апельсин']['цена'] # 100. Получение цены апельсина.
products['банан'] # {'цена': 110, 'вес': 1}. Получение характеристик (словаря) для банана.
banan = products['банан'] # Можно записать промежуточный результат в переменную
banan['вес'] # 1. А затем получить эти данные из переменной
