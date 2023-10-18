def speed(base, degree):
    if degree == 0:
        return 1
    if degree % 2 == 0:
        x = speed(base, degree // 2)
        return x * x
    return base * speed(base, degree - 1)
base = int(input("Введите основание: "))
degree = int(input("Введите степень: "))
result = speed(base, degree)
print(f"Результат: {result}")