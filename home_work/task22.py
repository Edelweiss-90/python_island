#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................

vowels = "аеёиоуыэюя"
result = {}
text: str
with open('dump.txt', 'r') as file:
    text = file.read().lower()

for letter in text:
    if letter not in vowels:
        continue

    val = result.get(letter)
    if val is not None:
        result.update({letter: val + 1})
    else:
        result.update({letter: 0})

print(result)
