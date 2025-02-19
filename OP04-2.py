import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal

if __name__ == "__main__":
    side = float(input("Введите длину стороны квадрата: "))
    result = square(side)
    print(f"Периметр квадрата: {result[0]}")
    print(f"Площадь квадрата: {result[1]}")
    print(f"Диагональ квадрата: {result[2]}")