def evclid(a, b):
    if b == 0:
        return a
    else:
        return evclid(b, a % b)
num1 = int(input("первое число: "))
num2 = int(input("второе число: "))
result = evclid(num1, num2)
print("наибольший обий делитель:", result)