s =input('Введите числа через пробел ')
a = b = c = None
current_variable = ''
variable_index = 1
for char in s:
    if char != ' ':
        current_variable += char
    else:
        if current_variable:
            if variable_index == 1:
                a = int(current_variable)
            elif variable_index == 2:
                b = int(current_variable)
            elif variable_index == 3:
                c = int(current_variable)
            variable_index += 1
            current_variable = ''  
if variable_index == 3:
        c = int(current_variable)
assert -1000 < a < 1000, "Неверное значение a"
assert -1000 < b < 1000, "Неверное значение b"
assert -1000 < c < 1000, "Неверное значение c"
if (a > b):
    if (c > a): print (a)
    elif (c > b): print (c)
    else: print(b)
elif (c > b):print (b)
else:
    if (a> c):print(a)
    else:print (c)

