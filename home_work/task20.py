#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""

with open('import_this.txt', 'w+') as file:
    file.write(text)
    file.seek(0)
    str_list = file.readlines()

    for i, value in enumerate(str_list[::-1]):
        print(value.replace('\n', ''))
