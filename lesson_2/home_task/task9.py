# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

def solution(A: int, B: int) -> float:
    return -B / A

A = int(input())
B = int(input())

solution = solution(A, B)
print(solution)
