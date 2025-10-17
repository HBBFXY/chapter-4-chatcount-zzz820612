# 从键盘输入一行字符
s = input()

# 初始化计数器
letters = 0    # 英文字符计数器
digits = 0     # 数字计数器
spaces = 0     # 空格计数器
others = 0     # 其他字符计数器

# 遍历每个字符进行统计
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1

# 按照要求的格式输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
