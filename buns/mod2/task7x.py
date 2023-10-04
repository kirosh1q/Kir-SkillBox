s = input("Строки из 0 и 1: ")
count_0 = s.count('0')
count_1 = s.count('1')

if count_0 == count_1:
    print("yes")
else:
    print("no")