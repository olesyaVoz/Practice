num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
num3 = int(input("Введите третье число:"))

if num1 < num2 > num3:
    print("Наибольшее число:", num2)
    print(num2)
elif num2 < num1 > num3:
    print("Наибольшее число:", num1)
    print(num1)
else:
    print("Наибольшее число:", num3)
    print(num3)

if num1 < num2 < num3 or num3 < num2 < num1:
    print(num2)
elif num2 < num1 < num3 or num3 < num1 < num2:
    print(num1)
else:
    print(num3)

if num1 > num2 < num3:
    print(num2)
elif num2 > num1 < num3:
    print(num1)
else:
    print(num3)
