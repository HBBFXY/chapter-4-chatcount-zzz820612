# 初始化各类型字符计数器
letter_count = 0    # 英文字符计数
digit_count = 0     # 数字计数
space_count = 0     # 空格计数
other_count = 0     # 其他字符计数

# 获取用户输入
user_input = input()

# 遍历输入字符串中的每个字符
for char in user_input:
    if char.isalpha():
        # 英文字符（a-z, A-Z）
        letter_count += 1
    elif char.isdigit():
        # 数字字符（0-9）
        digit_count += 1
    elif char.isspace():
        # 空格字符
        space_count += 1
    else:
        # 其他字符（中文、标点符号等）
        other_count += 1

# 按照指定格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
