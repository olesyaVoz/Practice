transfers = ["Здорово жить", "Шеф", "Орел и Решка", "Голос"]
for i in transfers:
    print(i)
s = str(input("Введите название телепередачи:"))
id = int(input("Введите позицию:"))
transfers.insert(id, s)
print(transfers)
