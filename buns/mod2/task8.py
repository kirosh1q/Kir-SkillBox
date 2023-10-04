input_data = input("Введите строку и символ через запятую без пробела: ")
comma_index = input_data.index(",")
s = input_data[:comma_index]
i = input_data[comma_index+1:]
count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break
print(count)
