input_str = input("Введите строку: ")
input_str = input_str.lower()
glas = 0
soglas = 0
for char in input_str:
    if char in 'ауоыэяюёиебвгджзйклмнпрстфхцчшщ':
        if char in 'ауоыэяюёие':
            glas += 1
        else:
            soglas += 1
print(glas, soglas)
