list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1)) # map(функция к которую мы хотим применить к каждому объекту и сам объект)
print(list_1)

"""Пример преобразование строки в числа"""

data = '15 156 96 3 5 8 52 5'

data = list(map(int, data.split())) # указывает, что 'data' это список, через функцию map передаем что иы хотим получить и объект, где разделителем объекта играет " "
print(data)