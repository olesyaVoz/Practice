n = int(input("Введите число: "))
def fib(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        c = a
        a = b
        b = c + a
    return fib_list
result = fib(n)
print("Последовательность чисел Фиббоначи, не привышающих ", n, ":",  result)