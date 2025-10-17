# 从键盘输入一行字符
text = input()
dscds132  *&……
# 初始化计数器
english_chars = 0
digits = 0
spaces = 0
other_chars = 0

# 遍历每个字符并统计
for char in text:
    if char.isalpha():  # 英文字符
        english_chars += 1
    elif char.isdigit():  # 数字
        digits += 1
    elif char.isspace():  # 空格
        spaces += 1
    else:  # 其他字符
        other_chars += 1

# 按照要求的格式输出
print("英文字符：" + str(english_chars))
print("数字：" + str(digits))
print("空格：" + str(spaces))
print("其他字符：" + str(other_chars))
