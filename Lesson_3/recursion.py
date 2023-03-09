def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

lst = []
for i in range(1,10):
    lst.append(fib(i))
print(lst )
