# 这个文件用于编写代码
# 从键盘输入一行字符
text = input("请输入一行字符：")

# 初始化计数器
letters = 0  # 英文字符
digits = 0   # 数字
spaces = 0   # 空格
others = 0   # 其他字符

# 遍历每个字符并统计
for char in text:
    if char.isalpha():  # 判断是否为英文字母
        letters += 1
    elif char.isdigit():  # 判断是否为数字
        digits += 1
    elif char.isspace():  # 判断是否为空格
        spaces += 1
    else:  # 其他字符
        others += 1

# 输出结果
print(f"英文字符：{letters}")
print(f"数字：{digits}")
print(f"空格：{spaces}")
print(f"其他字符：{others}")
