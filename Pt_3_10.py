s = input("Введите строку: ")
dictionary = {char: string.count(char) for char in s if char != " "}
print(dictionary)
