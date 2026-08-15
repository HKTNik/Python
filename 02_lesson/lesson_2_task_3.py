import math


def square(side):
    area = side * side
    return math.ceil(area)


side = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")
