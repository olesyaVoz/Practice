import itertools

nums = list(map(int, input("Введите числа: ").split()))
value = int(input("Введите число: "))


def combinations(nums, value):
    combinations = []
    for i in range(1, len(nums) + 1):
        for combination in itertools.combinations(nums, i):
            if sum(combination) == value:
                combinations.append(combination)
    return combinations


result = combinations(nums, value)
print(result)
