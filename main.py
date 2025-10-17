# 从键盘输入一行字符
s = input()

# 初始化计数器
letters = 0    # 英文字符计数器
digits = 0     # 数字计数器
spaces = 0     # 空格计数器
others = 0     # 其他字符计数器

# 遍历每个字符进行统计
for char in s:
    # 仅当字符是a-z或A-Z时才视为英文字符
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        letters += 1
    # 数字仅统计0-9
    elif '0' <= char <= '9':
        digits += 1
    # 空格仅统计半角空格
    elif char == ' ':
        spaces += 1
    # 其他所有字符
    else:
        others += 1

# 按照要求的格式输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
