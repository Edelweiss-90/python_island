#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input())
B = int(input())
C = int(input())

def calculate(a: int, b: int, c: int) -> None:
    AC = a - b
    BC = b - c
    
    print(AC, BC, AC + BC)
    
calculate(A, B, C)
