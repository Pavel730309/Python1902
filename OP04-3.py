def bank(a, years):
    for year in range(years):
        a += a * 0.1
    return a

if __name__ == "__main__":
    a = float(input("Введите сумму вклада: "))
    years = int(input("Введите количество лет: "))
    result = bank(a, years)
    print(f"Итоговая сумма на счету после {years} лет составит: {result:.2f} рублей")