# main.py

text = input()

english_chars = 0
digits = 0
spaces = 0
other_chars = 0

for char in text:
    if char.isalpha():
        english_chars += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        other_chars += 1

print(f"英文字符：{english_chars}")
print(f"数字：{digits}")
print(f"空格：{spaces}")
print(f"其他字符：{other_chars}")
