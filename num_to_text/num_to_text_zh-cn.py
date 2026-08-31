import sys

font = {
    "+": "正",
    "-": "负",
    "0": "零",
    "1": "一",
    "2": "二",
    "3": "三",
    "4": "四",
    "5": "五",
    "6": "六",
    "7": "七",
    "8": "八",
    "9": "九",
}

def is_int(num: str):
    """判断一个数是否是整数"""
    try:
        int(num)
        return True
    except ValueError:
        return False
def str_end0(num: str):
    """判断字符串末尾连续0的数量"""
    count = 0
    for val in num[::-1]:
        if val == "0":
            count += 1
        else:
            break
    return count

num = input()
if num[0] in "+-":
    op = num[0]
else:
    op = False

error = False
if len(num) > 10:
    print(f"错误: {num}数字位数超过10位")
    error = True

if not is_int(num):
    print(f"错误: {num}不是整数。")
    error = True

if len(num) >= 2 and (num[0] == "0" or num[1] == "0" and num[1] in "+-"):
    print(f"错误: {num}整数部分开头不能是0。")
    error = True

if len(num) >= 2 and num[1] == "0" and num[0] in "+-":
    print(f"错误: 0没有符号。")
    error = True

if error:
    sys.exit()

tokens = []
count = 0
token = ""
for val in num[::-1]:
    if val in "+-":
        break
    if count and count % 4 == 0:
        tokens.append(token[::-1])
        token = ""
        count = 0

    token += val
    count += 1

if token:
    tokens.append(token[::-1])

tokens2 = []
ji_shu = ["", "十", "百", "千"]
shu_ji = ["", "万", "亿"]
i = 0
while i < len(tokens):
    all0_4 = False
    if tokens[i] == "0000":
        all0_4 = True
    token = ""
    j = 0
    l0 = False
    while j < len(tokens[i]) - str_end0(tokens[i]) or tokens[i] == "0" and j == 0:
        ji_shu_i = len(tokens[i]) - j - 1
        digit = tokens[i][j]
        if digit == "0" and l0: 
            j += 1
            continue
        if not (digit == "1" and ji_shu_i == 1):
            token += font[digit]
        l0 = True
        if digit != "0":
            l0 = False
            token += ji_shu[ji_shu_i]
        j += 1
    if not all0_4:
        tokens2.append(token + shu_ji[i])
    i += 1

if op:
    print(font[op], end="")
for val in tokens2[::-1]:
    print(val, end="")