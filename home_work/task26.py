#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def convert_to_int(string: str):
    return list(map(lambda a: int(a), string.split(' ')))


def all_equal(lst):
    print(lst)
    return len(lst) == 1


def load_matrix(filename: str):
    with open(filename, 'r') as file:
        data = file.read().split('\n')
        data = list(map(convert_to_int, data))
        return data if len(set([len(item) for item in data])) == 1 else False


print(load_matrix('matrix.txt'))
