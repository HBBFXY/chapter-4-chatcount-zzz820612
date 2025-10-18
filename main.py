# 初始化各类字符的计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 获取用户输入的一行字符
s = input()

# 遍历输入的字符串，统计各类字符数量
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
