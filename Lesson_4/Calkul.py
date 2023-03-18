'КАЛЬКУЛЯТОР, СПОСОБЫ ЗАПИСИ ФУНКЦИИ'

def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y): 
    # op- operation (может хранить в себе функцию в данном случае сложение или умножение)
    print(op(x, y))

math(calc2, 5, 45) 

'Способ в одну строчку через анонимная переменную'
calc1 = lambda a,b: a + b

'Пример функции в принте'
math(lambda a,b: a + b, 5, 45)