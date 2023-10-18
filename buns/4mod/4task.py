def cpalindrome(word):
    char_counts = {}
    odd_count = 0
    for char in word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return None
        palindrome = ""
        middle_char = ""
    for char, count in char_counts.items():
        if count % 2 == 0:
            palindrome += char * (count // 2)
        else:
            middle_char = char
            palindrome += middle_char + palindrome[::-1]
            return palindrome
word = input("Введите слово: ")
result = cpalindrome(word)
if result:
    print("Можно составить палиндром: ", result)
else:
    print("Нельзя составить палиндром")