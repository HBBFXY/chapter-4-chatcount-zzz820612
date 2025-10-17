def main():
    # 从键盘输入一行字符
    s = input()
    
    # 初始化计数器
    english = 0
    digit = 0
    space = 0
    other = 0
    
    # 统计字符
    for char in s:
        if char.isalpha():
            english += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        else:
            other += 1
    
    # 输出结果
    print("英文字符：" + str(english))
    print("数字：" + str(digit))
    print("空格：" + str(space))
    print("其他字符：" + str(other))

if __name__ == "__main__":
    main()
