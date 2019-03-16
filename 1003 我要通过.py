###################################################

# “答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。

# 得到“答案正确”的条件是：

#     字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
#     任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
#     如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。

# 现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。
# 输入格式：

# 每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。
# 输出格式：

# 每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。
# 输入样例：

# 8
# PAT
# PAAT
# AAPATAA
# AAPAATAAAA
# xPATx
# PT
# Whatever
# APAAATAA

# 输出样例：

# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO

#####################################################

n = int(input())
m = n
s = []

while n > 0:
    s.append(input())
    n -= 1

key = {'P': True, 'A': True, 'T': True}

for i in range(m):
    j = 0
    lenth = len(s[i])
    while j < lenth and key.get(s[i][j], False):
        if s[i][j] == 'P':
            key['P'] = False
        if s[i][j] == 'T':
            key['T'] = False
        j += 1
    if j != lenth:
        print('NO')
        key['P'] = True
        key['T'] = True
        continue
    pL = s[i].find('P')
    tL = s[i].find('T')
    if (pL+1 >= tL) or ((lenth-tL-1)-(tL-pL-1)*pL) < 0:
        print('NO')
        key['P'] = True
        key['T'] = True
        continue
    print('YES')
    key['P'] = True
    key['T'] = True
