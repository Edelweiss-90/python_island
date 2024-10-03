# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".

def comparison(num: int) -> bool:
    st = str(num)
    return st == st[::-1]

number = int(input())

print(comparison(number))
