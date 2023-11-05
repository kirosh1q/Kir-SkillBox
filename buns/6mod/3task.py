def armstrong():
    n = 153
    while 1:
        digits = [int(x) for x in str(n)]
        num_digits = len(digits)
        sum_of_powers = sum([x ** num_digits for x in digits])
        if sum_of_powers == n and n not in range(2, 10):
            yield n
        n += 1  
generator = armstrong()

def get_armstrong_num():
    return next(generator)
for i in range (8):
    print(get_armstrong_num(), end=' ')
        