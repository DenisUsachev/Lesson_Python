"""Функции высшего порядка, работа с файлами"""

def f(x):
    return x * x
print(f(5)) # 25
print(type(f)) # finction

a = f # Переменная 'a' хронит в себе ссылку на функцию 'f'

print(type(a)) # finction
print(a(5)) # 25
