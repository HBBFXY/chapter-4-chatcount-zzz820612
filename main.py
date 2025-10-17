# 从键盘输入一行字符
text = input("请输入一段字符：sdfgg534  @#￥%")

# 初始化计数器
english_chars = 0
digits = 0
spaces = 0
other_chars = 0

# 遍历每个字符并统计
for char in text:
    if char.isalpha():  # 英文字符（包括大小写字母）
        english_chars += 1
    elif char.isdigit():  # 数字
        digits += 1
    elif char.isspace():  # 空格（包括普通空格、制表符等空白字符）
        spaces += 1
    else:  # 其他字符，如标点符号等
        other_chars += 1

# 按照要求的格式输出
print("英文字符：{}".format(english_chars))
print("数字：{}".format(digits))
print("空格：{}".format(spaces))
print("其他字符：{}".format(other_chars))
