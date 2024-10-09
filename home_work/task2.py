# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
print(int(age), int(foo[:2]))

# Преобразуйте переменную age в Boolean
age = "123abc"
print(bool(age))

# Преобразуйте переменную flag в Boolean
flag = 1
print(bool(flag))

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
print(bool(str_one), bool(str_two))

# Преобразуйте значение 0 и 1 в Boolean
print(bool(0), bool(1))

# Преобразуйте False в строку
print(str(False))
