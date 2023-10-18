def check_numbers(numbers):
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"
numbers = []
n = int(input("количество чисел "))
for i in range(n):
    num = int(input("введите число " ))
    numbers.append(num)
    result = check_numbers(numbers)
print(result)