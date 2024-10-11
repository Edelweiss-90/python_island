#todo: Дописать игру "Поле чудес"
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "подсказка 1", "плдсказка 2" ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.

# Пример вывода:

"Это слово обозначает наименьшую автономную часть языка программирования"

# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

# Введите букву: O

# O  ▒  ▒  ▒  ▒  ▒  O  ▒


# Введите букву: Я

# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

from random import randint

attempt = 10


def get_word() -> dict:
    length = len(words) - 1
    index = randint(0, length)

    word = words[index]

    return {
        'word': word,
        'mystery': ['.'] * len(word),
        'index': index
    }


data = get_word()


def find_index(index, letter, word) -> int:
    return word.index(letter, index)


while attempt:
    print(desc_[data.get('index')])

    letter = input('Letter:')
    word = data.get('word')
    mystery = data.get('mystery')

    if letter in word:
        index = word.index(letter)
        count = word.count(letter)

        if count > 1:
            tmp_index = index
            for i in range(count):
                mystery[find_index(tmp_index, letter, word)] = letter
                tmp_index += 1
        else:
            mystery[index] = letter

        if '.' not in mystery:
            print(''.join(mystery))
            print('Win')
            break

        print(mystery)
    else:
        attempt -= 1
        print(f'Attempt: {attempt}')

else:
    print('loss')
