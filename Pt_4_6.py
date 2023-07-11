alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
s = input("Введите строку: ")
key = int(input("Введите ключ: "))
new_s = ""
for letter in s:
    position = alphabet.find(letter)
    new_position = position + key
    if key > 33:
        print("Ошибка")
        break
    elif letter in alphabet:
        new_s += alphabet[new_position]
    else:
        new_s += letter
print(new_s)
