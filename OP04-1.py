def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

if __name__ == "__main__":
    start = int(input("Введите начальное значение: "))
    end = int(input("Введите конечное значение: "))
    result = sum_range(start, end)
    print(f"Сумма всех целых чисел от {start} до {end} включительно равна: {result}")