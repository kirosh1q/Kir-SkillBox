input_str = input("")
comma_index = input_str.index(',')
space_index = input_str.index(' ')
char = input_str[:space_index]
shift = int(input_str[space_index+1:])
char = input_str[:comma_index].strip()
shift = int(input_str[comma_index+1:].strip())
char = char.lower()
char_value = ord(char)
new_char_value = char_value + shift
if new_char_value > ord('z'):
    new_char_value = new_char_value - 26
elif new_char_value < ord('a'):
    new_char_value = new_char_value + 26
new_char = chr(new_char_value)
print(new_char)