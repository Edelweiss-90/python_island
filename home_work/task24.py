#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = 'abcdefghijklmnopqrstuvwxyz'

code_one = '8 5 12 12 15'
code_two = '8 5 12 12 15 , 0 23 15 18 12 4 !'


def create_word(input: str):
    code = input.split(' ')
    result = ''

    for symbol in code:
        if symbol.isdigit():
            num = int(symbol)
            if num == 0:
                continue

            result += alphabet[int(symbol) - 1]
        else:
            result += f'{symbol} '

    return result.strip()


print(create_word(code_one))
print(create_word(code_two))
