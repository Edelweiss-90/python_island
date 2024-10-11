# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

print('Сортировка по')
print("1. возрасту")
print("2. первой букве")
print("3. группе")


def sort_age(e):
    return e['age']

def sort_login(e):
    return e['login']

def sort_group(e):
    return e['group']


def filter_users(users, sort_type, criteria):
    if sort_type == 1:
        filtered_users = [user for user in users if user['age'] > criteria]
        filtered_users.sort(key=sort_age)

    elif sort_type == 2:
        filtered_users = [user for user in users if user['login'][0] == criteria]
        filtered_users.sort(key=sort_login)

    elif sort_type == 3:
        filtered_users = [user for user in users if user['group'] == criteria]
        filtered_users.sort(key=sort_group)

    return filtered_users


sort_type = int(input("тип сортировки:"))

if sort_type == 1:
    criteria = int(input("минимальный возраст:"))
elif sort_type == 2:
    criteria = input("первую букву логина:").capitalize()
elif sort_type == 3:
    criteria = input("группу (admin, guest, master):").lower()

filtered_users = filter_users(users, sort_type, criteria)

print(filtered_users)
