def count_characters(text):
    english_chars = 0
    digits = 0
    spaces = 0
    other_chars = 0

    for char in text:
        if char.isascii() and char.isalpha():  # 判断是否是英文字符（只限ASCII范围内的字母）
            english_chars += 1
        elif char.isdigit():  # 判断是否是数字
            digits += 1
        elif char.isspace():  # 判断是否是空格
            spaces += 1
        else:  # 其他字符
            other_chars += 1
    
    return english_chars, digits, spaces, other_chars

if __name__ == "__main__":
    text = input()  # 从键盘输入一行字符
    english_chars, digits, spaces, other_chars = count_characters(text)

    # 输出结果
    print(f"英文字符: {english_chars}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {other_chars}")
