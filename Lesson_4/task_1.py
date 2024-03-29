"""В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)"""

array = [1, 2, 3, 5, 8, 15, 23, 38]
res = []
for i in array:
    if i % 2 == 0:
        res.append((i, i ** 2)) # кортеж, поэтому в двойных скобках, с одной работать не будет
        
print(*res)


""""Функцией"""

def select(f, col): # расписание функции map
    return[f(x) for x in col] #Возвращает список в котором мы к каждому элементу применили "f"

array = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, array)
print(res) # Будут всё числа переводиться в int

def where(f,col):
    return[x for x in col if f(x)] # будет возвращет проверку 'f' от 'x'

res = where(lambda x: x % 2 == 0, res) # выборка которая принимает значение 'x' и возвращает True or False, где, если True, то возращает подходящее число 
print(res) # Будут только чётные числа

res = list(select(lambda x: (x, x ** 2), res)) # Преобразовать список 'res', как кортеж из числа и числа в квадрат
print(res)

""""Через встроенные функции"""
array = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, array) # Будут всё числа переводиться в int

res = filter(lambda x: x % 2 == 0, res) # выборка которая принимает значение 'x' и возвращает True or False, где, если True, то возращает подходящее число 
print(res) # Будут только чётные числа

res = list(map(lambda x: (x, x ** 2), res)) # Преобразовать список 'res', как кортеж из числа и числа в квадрат
print(res)