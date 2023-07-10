start = int(input("Введите начало диапазона: "))
finish = int(input("Введите конец диапазона: "))


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print([x for x in range(start, finish + 1) if prime(x)])
