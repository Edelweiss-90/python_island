#todo: Заданы множества
# все пользователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

# Вычислить пользователей online
all_users.difference_update(offline_users)
print(f'Result: {all_users}')


#todo: Заданы множества
#Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

print(f'Result: {readers_books.intersection(readers_magazines)}')
# Найти пользователей кто читает и книги и газеты