import unicodedata

def count_chars():
    s = input()
    
    letters = 0    # 严格匹配A-Za-z
    digits = 0     # 0-9数字
    spaces = 0     # 所有Unicode空格字符
    others = 0     # 其他字符
    
    for char in s:
        # 严格判断英文字母（仅A-Za-z）
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            letters += 1
        # 判断数字（仅0-9）
        elif '0' <= char <= '9':
            digits += 1
        # 判断所有类型的空格（包括半角、全角空格等）
        elif unicodedata.category(char) == 'Zs':
            spaces += 1
        # 其他字符
        else:
            others += 1
    
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")

count_chars()
